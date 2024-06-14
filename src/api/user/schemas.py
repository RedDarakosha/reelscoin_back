from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    tg_id: int
    is_bot: bool
    first_name: str
    last_name: str | None = None
    username: str | None = None
    language_code: str | None = None
    is_premium: bool | None = None
    photo_url: str | None = None
