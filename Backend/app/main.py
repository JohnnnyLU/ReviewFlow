from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database_helper import db_helper, get_db
from app.core.config import settings

from sqlalchemy import text, select

from app.models.business import Business

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    await db.execute(text("SELECT 1"))
    return {"status": "ok"}