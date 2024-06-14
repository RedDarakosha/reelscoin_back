import uvicorn

from src.core.settings import settings
from src.app import create_app


if __name__ == "__main__":
    uvicorn.run(
        create_app(settings),
        host=settings.server_settings.app_host,
        port=settings.server_settings.app_port,
    )
