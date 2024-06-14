from asyncpg.pool import Pool

from src.core.db.conn import DBConnection


class DBPool(Pool):
    def __init__(self, *args, **kwargs):
        print("zxc")
        super().__init__(*args, **kwargs)


async def acquire_conn(pool):
    async with pool.acquire() as conn:
        yield conn
