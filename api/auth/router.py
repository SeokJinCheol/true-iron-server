from fastapi import APIRouter

from core.security import create_access_token

authRouter = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@authRouter.post('/login')
async def login():
    return {'token': create_access_token({'test': 'test'})}