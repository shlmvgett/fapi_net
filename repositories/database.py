from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:admin@postgres/postgres"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
SessionLocal = async_sessionmaker(engine, autoflush=True, expire_on_commit=False)

Base = declarative_base()
