# AuthRouter receives the request
# don’t need an interface for your router. Routers should remain thin, framework-bound, and wired with injected services. That’s clean, composable, and testable enough for even large-scale apps.
# It should NOT hash passwords itself
# It should NOT access repositories directly
# It should NOT contain business logic
# Instead, it delegates everything to AuthServiceInterface

from fastapi import APIRouter, status, Depends
from features.login.schemas.auth_schemas import RegisterRequest, LoginRequest, TokenResponse
from features.login.services.auth_service_interface import AuthServiceInterface

def get_auth_router(auth_service: AuthServiceInterface) -> APIRouter:
    router = APIRouter(prefix="/auth", tags=["Auth"])

    @router.post("/register", status_code=status.HTTP_201_CREATED)
    def register_user(data: RegisterRequest):
        auth_service.register_user(email=data.email, password=data.password)
        return {"message": "User registered successfully"}

    @router.post("/login", response_model=TokenResponse)
    def login_user(data: LoginRequest):
        token = auth_service.login_user(email=data.email, password=data.password)
        return TokenResponse(access_token=token)

    return router
