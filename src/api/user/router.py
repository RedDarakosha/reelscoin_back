from fastapi import APIRouter, Depends
from asyncpg import Connection

from dependency_injector.wiring import inject, Provide

from src.api.user.schemas import UserCreateSchema
from src.api.user.repository import UserRepository

from src.utils.exceptions.api import UserValidationError
from src.core.di_container import Container

user_router = APIRouter(prefix="/user")


@user_router.get("/")
def ping():
    return {"status": "ok"}


@user_router.post("/add")
async def user_add(user_create_schema: UserCreateSchema):
    if user_create_schema.is_bot:
        raise UserValidationError(400, detail="User must be not a bot")
    return await UserRepository.add_user(user_create_schema)
