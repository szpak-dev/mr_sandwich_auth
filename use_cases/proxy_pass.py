import httpx
from fastapi import Request, HTTPException

from domain.errors import SessionNotFound, JwtClaimsNotFound, IdentityNotFound
from domain.services import extract_session_id
from adapters.driving import http_proxy_pass


async def proxy_pass_action(request: Request):
    try:
        session_id = extract_session_id(request)
    except IdentityNotFound as e:
        raise HTTPException(status_code=401, detail=str(e))

    try:
        jwt_claims = http_proxy_pass.authenticate(session_id)
    except (SessionNotFound, JwtClaimsNotFound) as e:
        raise HTTPException(status_code=401, detail=str(e))

    headers = http_proxy_pass.append_jwt_to_headers(
        jwt_claims,
        dict(request.headers.items()),
    )

    with httpx.Client() as client:
        try:
            return client.request(
                method=request.method,
                url=str(request.url),
                content=await request.body(),
                headers=headers,
                params=request.query_params,
            )
        except httpx.HTTPError as e:
            print(str(e))
