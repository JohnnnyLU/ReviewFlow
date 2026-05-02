from app.core.database_helper import db_helper


async def get_db():
    async for session in db_helper.get_session():
        yield session