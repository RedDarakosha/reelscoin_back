from asyncpg import Connection
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.api.user.repository import UserRepository
from src.api.user.schemas import UserCreateSchema
from src.core.di_container import Container
from src.utils.exceptions.api import UserValidationError

user_router = APIRouter(prefix="/user")


@user_router.get("/")
def ping():
    return {"status": "ok"}


@user_router.post("/add")
async def user_add(user_create_schema: UserCreateSchema):
    if user_create_schema.is_bot:
        raise UserValidationError(400, detail="User must be not a bot")
    return await UserRepository.add_user(user_create_schema)


@user_router.get("/all")
async def get_all_users():
    return await UserRepository.get_all_users()


@user_router.get("/cache")
async def get_all_cache():
    return await UserRepository.get_all_cache()


@user_router.post("/cache/user")
async def get_cache_by_id(tg_id: int):
    return await UserRepository.get_cache_by_id(tg_id)
