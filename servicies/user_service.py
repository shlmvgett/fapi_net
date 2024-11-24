from fastapi import HTTPException

from models import User
from repositories import user_repository
from repositories.database import SessionLocal
from repositories.db_models import UserDB


class UserService:

    @staticmethod
    async def auth_user(form_data, db: SessionLocal) -> UserDB:
        rs = await user_repository.UsersRepository.get_by_email(db=db, email=form_data.username)
        if not rs:
            raise HTTPException(status_code=400, detail="Incorrect login")
        if rs.password != form_data.password:
            raise HTTPException(status_code=400, detail="Incorrect login")
        return rs

    @staticmethod
    async def create_new_user(user: User, db: SessionLocal):
        rs = await user_repository.UsersRepository.get_by_email(db=db, email=user.email)
        if rs:
            raise HTTPException(status_code=400, detail="User with email already exist")
        return await user_repository.UsersRepository.create(db=db, user=user)

    @staticmethod
    async def get_user_by_email(email: str, db: SessionLocal):
        rs = await user_repository.UsersRepository.get_by_email(db=db, email=email)
        if not rs:
            raise HTTPException(status_code=400, detail=f"User with id: {email} no found")
        return rs

    @staticmethod
    async def get_user_by_id(user_id: int, db: SessionLocal):
        rs = await user_repository.UsersRepository.get_by_id(db=db, user_id=user_id)
        if not rs:
            raise HTTPException(status_code=400, detail=f"User with id: {user_id} no found")
        return rs

    @staticmethod
    async def get_all_users(db: SessionLocal):
        return await user_repository.UsersRepository.all(db=db)



