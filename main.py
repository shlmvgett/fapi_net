import json
from typing import Annotated, Any

from fastapi import FastAPI, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request

from orm import crud, models
from orm.database import SessionLocal, engine, Base

app = FastAPI()


@app.get("/api/v1/ping")
async def ping():
    return {"message": "pong"}


@app.get("/api/v1/user")
async def get_user():
    return {"message": "Hello World"}


@app.post("/api/v1/user")
async def create_user():
    return {"message": "Hello World"}


# @app.on_event("startup")
# async def init_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
# # Dependency
# async def get_db() -> SessionLocal:
#     async with SessionLocal() as session:
#         yield session
#
#
# @app.post("/users/")
# async def create_user(request: Request, db: SessionLocal = Depends(get_db)):
#     user = json.loads((await request.body()).decode('utf-8'))
#     db_user = await crud.Users.get_by_email(db, email=user['email'])
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return await crud.Users.create(db=db, email=user['email'], password=user['password'])

