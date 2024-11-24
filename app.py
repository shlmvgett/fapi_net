import logging
from datetime import timedelta, datetime, timezone
from typing import Annotated

import jwt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel
from starlette import status

from models import User
from repositories.database import SessionLocal
from servicies.user_service import UserService

SECRET_KEY = "5bcf29d6353fdd22fa1514d557fde47faffa3ce7d07eb00e7d893b92aab682de"  # not for prod
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


async def get_db() -> SessionLocal:
    async with SessionLocal() as session:
        yield session


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: SessionLocal = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = await UserService.get_user_by_email(email=token_data.username, db=db)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(form_data, db: SessionLocal):
    user = await UserService.get_user_by_email(email=form_data.username, db=db)
    if not user:
        return None

    if not verify_password(form_data.password, user.password):
        return None
    return user


@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: SessionLocal = Depends(get_db)) -> Token:
    user_bd = await authenticate_user(form_data, db)
    if user_bd:
        access_token = create_access_token(data={"sub": user_bd.email})
        return Token(access_token=access_token, token_type="bearer")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )


@app.get("/")
async def ping():
    return {"message": "ping"}


@app.get("/users/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user


@app.post("/api/v1/user")
async def create_user(user: User, db: SessionLocal = Depends(get_db)):
    return await UserService.create_new_user(user, db)


@app.get("/api/v1/user/{user_id}")
async def get_user(user_id: int, db: SessionLocal = Depends(get_db)):
    return await UserService.get_user_by_id(db=db, user_id=user_id)


@app.get("/api/v1/users")
async def get_users(db: SessionLocal = Depends(get_db)):
    return await UserService.get_all_users(db=db)
