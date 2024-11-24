from sqlalchemy.ext.asyncio import AsyncSession

from hash_utils import get_hash
from models import User
from sqlalchemy import select

from .db_models import UserDB


class UsersRepository:
    @staticmethod
    async def get_by_id(db: AsyncSession, user_id: int):
        return (await db.execute(select(UserDB).filter(UserDB.id == user_id))).scalars().first()

    @staticmethod
    async def get_by_email(db: AsyncSession, email: str):
        return (await db.execute(select(UserDB).filter(UserDB.email == email))).scalars().first()

    @staticmethod
    async def all(db: AsyncSession, skip: int = 0, limit: int = 100):
        return (await db.execute(select(UserDB).offset(skip).limit(limit))).scalars().all()

    @staticmethod
    async def create(db: AsyncSession, user: User):
        db_user = UserDB(name=user.name, last_name=user.last_name, email=user.email, password=get_hash(user.password).decode('utf-8'),
                         bday=user.bday, sex=user.sex, interests=user.interests, city=user.city)
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user
