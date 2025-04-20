from typing import Dict
from features.login.entities.user import UserEntity
from features.login.repositories.user_repository_interface import UserRepositoryInterface
from typing import Optional

class InMemoryUserRepository(UserRepositoryInterface):
    def __init__(self):
        self._users: Dict[str, UserEntity] = {}

    def get_by_email(self, email: str) -> Optional[UserEntity]:
        return self._users.get(email)

    def save(self, user: UserEntity) -> None:
        self._users[user.email] = user
