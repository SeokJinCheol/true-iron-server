import jwt
import os

from passlib.context import CryptContext
from dotenv import load_dotenv
from passlib.utils.handlers import parse_int
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

load_dotenv()

from datetime import timedelta, datetime
from time import timezone

async def get_user(db: AsyncSession, user_id: str):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=parse_int(os.getenv('JWT.ACCESS_TOKEN_EXPIRE_MINUTES')))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv('JWT.SECURITY_KEY'), algorithm=os.getenv('JWT.ALGORITHM'))
    return encoded_jwt