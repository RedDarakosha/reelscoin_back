import time

from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from pydantic import BaseModel
from redis import Connection as RedisConnection

from src.api.user.schemas import UserCreateSchema
from src.core.db import DBConnection
from src.core.di_container import Container
from src.core.settings import settings
from src.models.user import (User, UserProperties, user_from_string,
                             user_to_string)


class UserRepository(BaseModel):

    @classmethod
    @inject
    async def earn_points(
        cls, tg_id: int, conn: DBConnection = Depends(Provide[Container.connection])
    ):
        pass

    @classmethod
    @inject
    async def add_user(
        cls,
        user_create_schema: UserCreateSchema,
        conn: DBConnection = Depends(Provide[Container.connection]),
        cache: RedisConnection = Depends(Provide[Container.redis_cache]),
    ):
        user = await User.create_if_not_exists(user_create_schema, conn=conn)
        await cache.set(user.tg_id, user_to_string(user))
        return user

    @classmethod
    @inject
    async def get_all_users(
        cls,
        conn: DBConnection = Depends(Provide[Container.connection]),
    ):
        users: list[User] = await User.get_all(conn=conn)
        return users

    @classmethod
    @inject
    async def get_all_cache(
        cls, cache: RedisConnection = Depends(Provide[Container.redis_cache])
    ):
        cache = await cache.keys("*")
        print(cache)
        return cache

    @classmethod
    @inject
    async def get_cache_by_id(
        cls,
        tg_id: str,
        cache: RedisConnection = Depends(Provide[Container.redis_cache]),
    ):
        cache = await cache.get(tg_id)
        return cache

    @classmethod
    @inject
    async def claim_store(
        cls,
        tg_id: int,
        conn: DBConnection = Depends(Provide[Container.connection]),
        cache: RedisConnection = Depends(Provide[Container.connection]),
    ):
        user = await cache.get(tg_id)
        if not user:
            user = await User.get_by_tg_id(tg_id, conn=conn)
        else:
            user = user_from_string(user)

        if (
            user.last_earn + settings.game_settings.earn_timeout < time.time()
            or not user.last_earn
        ):
            await User.claim_coins(tg_id, conn=conn)

        return "ok"
