from src.api.game.router import game_router
from src.api.user.router import user_router

routers = [user_router, game_router]


def init_routes(app):
    for router in routers:
        app.include_router(router)
