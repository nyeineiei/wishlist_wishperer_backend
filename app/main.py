from fastapi import FastAPI
from features.login.routers.auth_router import get_auth_router
from features.login.repositories.in_memory_user_repository import InMemoryUserRepository
from features.login.services.auth_service import AuthService
from features.login.services.security import SecurityService
from features.login.services.token_service import TokenService

app = FastAPI()

# Instantiate core dependencies
user_repo = InMemoryUserRepository()
security_service = SecurityService()
token_service = TokenService()

# Inject into AuthService (high-level module depends on abstractions)
auth_service = AuthService(
    user_repo=user_repo,
    security_service=security_service,
    token_service=token_service
)

# Inject into router
auth_router = get_auth_router(auth_service)

# Register router
app.include_router(auth_router)
