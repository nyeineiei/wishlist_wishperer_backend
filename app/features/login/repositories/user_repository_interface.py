# Abstracts user storage
from abc import ABC, abstractmethod
from app.features.login.entities.user_entity import UserEntity
from typing import Optional

class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def save(self, user: UserEntity) -> None:
        pass