from redis.asyncio import Redis
from redis.asyncio.connection import ConnectionPool

from src.core.settings import RedisSettings


def create_redis_pool(settings: RedisSettings):
    pool = ConnectionPool.from_url(
        settings.redis_url, max_connections=settings.max_connections
    )
    return pool


def acquire_redis_conn(pool: ConnectionPool):
    return Redis(connection_pool=pool, decode_responses=True)
