from datetime import datetime
from pydantic import BaseModel
from asyncpg import Connection

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
    last_earn: datetime | None = None


class User(UserProperties):
    id: int

    @classmethod
    async def create_if_not_exists(
        cls, user_properties: UserProperties, conn: Connection
    ):
        print("MODELS")
        print(conn)
        print(conn._con)
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
            ON CONFLICT (tg_id) DO NOTHING;
        """

        try:
            result = await conn.execute(
                query,
                user_properties.tg_id,
                user_properties.first_name,
                user_properties.last_name,
                user_properties.username,
                user_properties.language_code,
                user_properties.is_premium,
                user_properties.photo_url,
            )
            return result
        except Exception as e:
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
    async def get_by_id(cls, tg_id: int, conn: Connection) -> "User":
        query = """
            SELECT FROM users(id, tg_id, first_name, username, amount) WHERE id=$1
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
