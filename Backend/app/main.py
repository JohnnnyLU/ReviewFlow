from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database_helper import db_helper

from app.api.deps import get_db
from sqlalchemy import text

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/health/db")
async def health_db():
    async with get_db() as db:
        result = await db.execute(text("SELECT 1"))
        value = result.scalar()

        return {
            "status": "ok" if value == 1 else "error",
            "db": "connected"
        }