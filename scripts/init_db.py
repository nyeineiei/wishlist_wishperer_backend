# scripts/init_db.py

import asyncio
from app.shared.database.engine import engine
from app.shared.database.base import Base
from app.features.login.repositories.models import user_model

import asyncio

async def init_db():
    print("🚧 Creating tables...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tables created.")

if __name__ == "__main__":
    asyncio.run(init_db())
