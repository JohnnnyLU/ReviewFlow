from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database_helper import db_helper, Base
from app.api.v1.router import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await conn.close()

app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix='/api/v1')