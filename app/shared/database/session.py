# get_db() dependency provider
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from app.shared.database.engine import engine
from fastapi import Depends

# Factory
async_session_factory = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency
async def get_db() -> AsyncSession:
    async with async_session_factory() as session:
        yield session
