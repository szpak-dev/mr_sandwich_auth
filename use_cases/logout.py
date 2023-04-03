from fastapi import Request, Response, HTTPException

from adapters.driving import http_auth_api
from domain.errors import IdentityNotFound, SessionNotFound
from domain.services import extract_session_id


async def logout_action(request: Request, response: Response):
    try:
        session_id = extract_session_id(request)
        http_auth_api.logout(session_id)

        response.delete_cookie('session_id')
        response.headers['Authorization'] = ''
    except IdentityNotFound:
        raise HTTPException(status_code=409, detail='No Identity found')
    except SessionNotFound:
        raise HTTPException(status_code=404, detail='Session not found')
