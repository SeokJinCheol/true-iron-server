from fastapi import APIRouter

authRouter = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@authRouter.post('/login')
async def login():
    return {'token': '<token>'}