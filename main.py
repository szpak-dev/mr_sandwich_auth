from fastapi import FastAPI, Request, Response

from use_cases.create_user import Registration, create_user_action
from use_cases.login import Credentials, login_action
from use_cases.logout import logout_action
from use_cases.get_logged_in_user import get_logged_in_user_action, User
from use_cases.proxy_pass import proxy_pass_action

methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
app = FastAPI(debug=True)


@app.post('/auth/users', status_code=201, tags=['User'])
async def create_user(registration: Registration):
    await create_user_action(registration)


@app.get('/auth/users', status_code=200, response_model=User, tags=['User'])
async def me(request: Request):
    return await get_logged_in_user_action(request)


@app.post('/auth/login', status_code=201, tags=['Session'])
async def login(response: Response, credentials: Credentials):
    return await login_action(credentials, response)


@app.delete('/auth/logout', status_code=204, tags=['Session'])
async def logout(request: Request, response: Response):
    await logout_action(request, response)


@app.api_route('/web_store_cart/{full_path:path}', methods=methods)
@app.api_route('/food_factory/{full_path:path}', methods=methods)
async def proxy_pass(full_path: str, request: Request):
    r = await proxy_pass_action(request)

    response = Response(
        r.content,
        r.status_code,
        r.headers,
    )

    return response
