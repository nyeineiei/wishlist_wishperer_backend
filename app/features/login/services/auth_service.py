#AuthService - handles business logic
# AuthService - handles business logic
from fastapi import HTTPException, status
from app.features.login.repositories.user_repository_interface import UserRepositoryInterface
from app.features.login.entities.user_entity import UserEntity
from app.features.login.services.auth_service_interface import AuthServiceInterface
from app.features.login.services.security_service_interface import SecurityServiceInterface
from app.features.login.services.token_service import TokenService

class AuthService(AuthServiceInterface):
    def __init__(
        self,
        user_repo: UserRepositoryInterface,
        security_service: SecurityServiceInterface,
        token_service: TokenService
    ):
        self.user_repo = user_repo
        self.security = security_service
        self.token = token_service

    # Validates uniqueness, hashes password, saves user
    async def register_user(self, email: str, password: str) -> None:
        existing_user = await self.user_repo.get_by_email(email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists"
            )

        hashed = self.security.hash_password(password)
        user = UserEntity(email=email, hashed_password=hashed)
        await self.user_repo.save(user)

    # Verifies credentials, returns JWT token
    async def login_user(self, email: str, password: str) -> str:
        user = await self.user_repo.get_by_email(email)
        if not user or not self.security.verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        return self.token.create_access_token({"sub": user.email})
