# from asyncio import

from asyncpg import create_pool

from .pool import DBConnection, DBPool, acquire_conn
from .record import DBRecord


async def init_db_pool(db_settings):
    pool = await create_pool(
        connection_class=DBConnection,
        record_class=DBRecord,
        min_size=db_settings.min_size,
        max_size=db_settings.max_size,
        dsn=db_settings.dsn,
    )
    return pool
