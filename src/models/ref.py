import base64

from asyncpg import Connection

from pydantic import BaseModel


class Referal(BaseModel):
    link: str
    tg_id: str

    @classmethod
    async def create(cls, tg_id: int, conn: Connection) -> "Referal":
        query = """
            INSERT INTO refs(tg_id, link) VALUES ($1, $2)
        """

        tg_id = str(tg_id).encode("ascii")
        encoded_id = base64.b64encode(tg_id)
        encoded_id = encoded_id.decode("ascii")

        link = f"https://t.me/ReelsCoinBot/app?startapp=ref_{encoded_id}"

        try:
            result = await conn.execute(query, tg_id, link)
        except Exception as e:
            print(tg_id, link)
            print(e)

        return cls(**result)

    @classmethod
    async def get_by_tg_id(cls, tg_id: int, conn: Connection):
        query = """
            SELECT tg_id, link FROM refs WHERE tg_id=$1
        """

        try:
            result = await conn.execute(query, tg_id)
        except Exception as e:
            print(e)

        return result
