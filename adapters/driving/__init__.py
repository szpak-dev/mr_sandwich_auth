from adapters import session_repository, user_repository, jwt_claims_repository
from adapters.driving.http_auth_api import HttpAuthApi
from adapters.driving.http_proxy_pass import HttpProxyPass
from adapters.driving.http_user_api import HttpUserApi

http_auth_api = HttpAuthApi(session_repository, user_repository, jwt_claims_repository)
http_user_api = HttpUserApi(user_repository)
http_proxy_pass = HttpProxyPass(session_repository, jwt_claims_repository)
