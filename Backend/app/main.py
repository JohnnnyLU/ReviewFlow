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

from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="My API",
        version="1.0.0",
        description="API with JWT",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    # добавляем по умолчанию для всех эндпоинтов
    for path in openapi_schema["paths"].values():
        for op in path.values():
            op.setdefault("security", []).append({"BearerAuth": []})
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi