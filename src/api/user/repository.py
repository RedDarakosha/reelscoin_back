from fastapi import Depends

from dependency_injector.wiring import Provide, inject
from pydantic import BaseModel

from src.core.di_container import Container
from src.models.user import User, UserProperties

from src.api.user.schemas import UserCreateSchema
from src.core.db import DBConnection


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
    ):
        user = await User.create_if_not_exists(user_create_schema, conn=conn)
        return user
