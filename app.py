from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models import User
from repositories.database import SessionLocal
from servicies.user_service import UserService

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_db() -> SessionLocal:
    async with SessionLocal() as session:
        yield session


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: SessionLocal = Depends(get_db)):
    r = await UserService.auth_user(form_data=form_data, db=db)
    return {"access_token": r.email, "token_type": "bearer"}


@app.get("/")
async def ping():
    return {"message": "ping"}


@app.post("/api/v1/user")
async def create_user(user: User, db: SessionLocal = Depends(get_db)):
    return await UserService.create_new_user(user, db)


@app.get("/api/v1/user/{user_id}")
async def get_user(user_id: int, db: SessionLocal = Depends(get_db)):
    return await UserService.get_user_by_id(db=db, user_id=user_id)


@app.get("/api/v1/users")
async def get_users(db: SessionLocal = Depends(get_db)):
    return await UserService.get_all_users(db=db)

