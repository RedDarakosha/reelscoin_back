from fastapi import FastAPI

from src.api.routers import init_routes
from src.core.di_container import init_container


class CryptoAPI(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def create_app(settings):
    app = CryptoAPI()
    init_routes(app)
    init_container(app)

    return app
