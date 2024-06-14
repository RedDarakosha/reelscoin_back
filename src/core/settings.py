from pydantic import BaseModel, Field

from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseModel):
    dsn: str = "postgres://reels:reels@localhost:5432/reels"
    max_size: int = Field(10)
    min_size: int = Field(10)


class ServerSettings(BaseModel):
    app_name: str = Field("reels")
    app_port: int = Field(8000)
    app_host: str = Field("localhost")
    debug: bool = Field(True)


class Settings(BaseSettings):
    server_settings: ServerSettings = ServerSettings()
    db_settings: DBSettings = DBSettings()

    model_config = SettingsConfigDict(env_file=".env")

    zxc: str = Field("test")


settings = Settings()
