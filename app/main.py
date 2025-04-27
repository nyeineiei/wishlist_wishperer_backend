from fastapi import FastAPI
from app.features.login.routers.auth_router import get_auth_router
from app.features.login.services.auth_service import AuthService
from app.features.login.services.security import SecurityService
from app.features.login.services.token_service import TokenService
from app.features.login.repositories.sqlite_user_repository import SQLiteUserRepository
from app.shared.database.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to wishlist_wishperer!"}

# ✅ Add auth router during app startup
@app.on_event("startup")
async def setup_routers():
    # get_db() is a generator, so we use async for to extract session
    async for db in get_db():
        user_repo = SQLiteUserRepository(db)
        security_service = SecurityService()
        token_service = TokenService()
        auth_service = AuthService(user_repo, security_service, token_service)
        router = get_auth_router(auth_service)

        app.include_router(router)
        break  # ✅ important! prevents generator exhaustion
