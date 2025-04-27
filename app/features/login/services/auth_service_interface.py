from abc import ABC, abstractmethod

class AuthServiceInterface(ABC):
    @abstractmethod
    def register_user(self, email: str, password: str) -> None:
        pass

    @abstractmethod
    def login_user(self, email: str, password: str) -> str:
        """Returns JWT access token"""
        pass
