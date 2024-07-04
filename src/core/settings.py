import datetime

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseModel):
    dsn: str = "postgres://reels:reels@postgres:5432/reels"
    max_size: int = Field(10)
    min_size: int = Field(10)


class ServerSettings(BaseModel):
    app_name: str = Field("reels")
    app_port: int = Field(8000)
    app_host: str = Field("0.0.0.0")
    debug: bool = Field(True)
    # allowed_host: str = "0.0.0.0"


# class CacheSettings(BaseModel):
#     # UserCache key expired after in seconds
#     user_cache_expired_at: int = 100


class RedisSettings(BaseModel):
    redis_url: str = "redis://redis:6379"
    max_connections: int = 5


class GameSettings(BaseModel):
    amount_number: int = 1000
    # user can earn reels every three hours
    earn_timeout: float = 60 * 60 * 3


class Settings(BaseSettings):
    server_settings: ServerSettings = ServerSettings()
    db_settings: DBSettings = DBSettings()
    redis_settings: RedisSettings = RedisSettings()
    game_settings: GameSettings = GameSettings()

    model_config = SettingsConfigDict(env_file=".app.env")


settings = Settings()
