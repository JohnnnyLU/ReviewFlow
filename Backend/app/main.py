from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.sessions import SessionMiddleware

from app.core.database_helper import db_helper, Base
from app.api.v1.router import api_router
from app.core.config import settings

# --- Lifespan ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await conn.close()

# --- App ---
app = FastAPI(lifespan=lifespan)

# --- Include router ---
app.include_router(api_router, prefix='/api/v1')

# --- Middleware ---
app.add_middleware(
    SessionMiddleware,  # type: ignore
    secret_key=settings.SESSION_MIDDLEWARE_SECRET_KEY,
)
