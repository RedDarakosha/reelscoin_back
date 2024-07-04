import time
from datetime import datetime

from asyncpg import Connection
from expiring_dict import ExpiringDict
from pydantic import BaseModel

from src.core.settings import settings
from src.models.ref import Referal


class UserProperties(BaseModel):
    tg_id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None
    language_code: str | None = None
    is_premium: bool | None = None
    photo_url: str | None = None

    amount: int = 0
    last_earn: float | None = None


class User(UserProperties):

    @classmethod
    async def get_all(cls, conn: Connection):
        query = """
            SELECT * from users;
        """
        try:
            result = await conn.fetch(query)
            return [cls(**user) for user in result]
        except Exception as e:
            print(e)

    @classmethod
    async def create_if_not_exists(
        cls, user_properties: UserProperties, conn: Connection
    ):
        query = """
            INSERT INTO users(
                tg_id,
                first_name,
                last_name,
                username,
                language_code,
                is_premium,
                photo_url
                )
            VALUES(
                $1,
                $2,
                $3,
                $4,
                $5,
                $6,
                $7
                )
            RETURNING *;
        """

        try:
            result = await conn.fetchrow(
                query,
                user_properties.tg_id,
                user_properties.first_name,
                user_properties.last_name,
                user_properties.username,
                user_properties.language_code,
                user_properties.is_premium,
                user_properties.photo_url,
            )
            print("\n" * 10)
            print(result)
            return cls(**result)
        except Exception as e:
            print("\n" * 10)
            print(e)

    @classmethod
    async def get_by_tg_id(cls, tg_id: int, conn: Connection) -> "User":
        query = """
            SELECT FROM users(id, tg_id, first_name, username, amount) WHERE tg_id=$1
        """
        try:
            result = await conn.execute(query.format(tg_id))
            return User(**result)
        except Exception as e:
            print(e)

    @classmethod
    async def create_referal(cls, tg_id: int, conn: Connection) -> Referal:
        ref = await Referal.create(tg_id, conn)
        return ref

    @classmethod
    async def clain_coins(cls, tg_id: int, conn: Connection):
        query = f"""
            UPDATE users
            SET amount = amount + {settings.game_settings.amount_number}, last_earn=to_timestamp($2)
            WHERE tg_id = $1
        """

        try:
            await conn.execute(query, tg_id, time.time())
            return True
        except Exception as e:
            print(e)


class UserCache:
    # expired_after in seconds
    def __init__(self, expired_after: int):
        self.cache = ExpiringDict(expired_after)

    def add(self, user: User):
        self.cache[user.tg_id] = user

    def check(self, tg_id: int) -> bool:
        return bool(self.cache.get(tg_id))

    def get(self, tg_id: int) -> User | None:
        return self.cache.get(tg_id)


def user_to_string(user: User) -> str:
    return f"{user.tg_id}:{user.first_name}:{user.last_name}:{user.username}:{user.language_code}:{user.is_premium}:{user.photo_url}:{user.amount}:{user.last_earn}"


def user_from_string(user: str) -> User:
    (
        tg_id,
        first_name,
        last_name,
        username,
        language_code,
        is_premium,
        photo_url,
        amount,
        last_earn,
    ) = user.split(":")
    return User(
        tg_id=tg_id,
        first_name=first_name,
        last_name=last_name,
        username=username,
        language_code=language_code,
        is_premium=is_premium,
        photo_url=photo_url,
        amount=amount,
        last_earn=last_earn,
    )
