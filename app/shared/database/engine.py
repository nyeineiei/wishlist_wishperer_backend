# Async engine creation
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from pathlib import Path

print(f"🧭 __file__ = {__file__}")

# ✅ Compute DB path at project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATABASE_PATH = BASE_DIR / "wishlist.db"
DATABASE_URL = f"sqlite+aiosqlite:///{DATABASE_PATH}"

print(f"🔍 Using DB at: {DATABASE_PATH}")

# ✅ Create async engine
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)
