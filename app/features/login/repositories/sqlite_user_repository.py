from typing import Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.features.login.entities.user_entity import UserEntity
from app.features.login.repositories.user_repository_interface import UserRepositoryInterface
from app.features.login.repositories.models.user_model import UserModel


class SQLiteUserRepository(UserRepositoryInterface):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> Optional[UserEntity]:
        result = await self.db.execute(
            select(UserModel).where(UserModel.email == email)
        )
        user = result.scalars().first()
        if user:
            return UserEntity(email=user.email, hashed_password=user.hashed_password)
        return None

    async def save(self, user: UserEntity) -> None:
        db_user = UserModel(
            email=user.email,
            hashed_password=user.hashed_password,
        )
        self.db.add(db_user)
        await self.db.commit()
