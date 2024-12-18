from fastapi import APIRouter

from util.security import create_access_token, decode_access_token

authRouter = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@authRouter.post('/login')
async def login():
    return {'token': create_access_token({'test': 'test'})}



@authRouter.post('/me')
async def get_token():
    return {'token': decode_access_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZXN0IjoidGVzdCIsImV4cCI6MTczMzAzMTYwN30.73vAY8Lj-F-xa42qf-c3UQg7nBvm4WDu92nSXaJlcsU")}