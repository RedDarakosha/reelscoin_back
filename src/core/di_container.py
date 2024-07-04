from dependency_injector import containers, providers

from src.core.db import acquire_conn, init_db_pool
from src.core.redis import acquire_redis_conn, create_redis_pool
from src.core.settings import Settings, settings
from src.models.user import UserCache


class Container(containers.DeclarativeContainer):
    # # wiring_config = containers.WiringConfiguration(
    # #     auto_wire=True
    # )

    config = providers.Configuration("config")

    pool = providers.Resource(init_db_pool, settings.db_settings)
    connection = providers.Resource(acquire_conn, pool)
    redis_pool = providers.Resource(create_redis_pool, settings.redis_settings)
    redis_cache = providers.Factory(acquire_redis_conn, redis_pool)
    # user_cache = providers.Resource(
    #     UserCache, settings.cache_config.user_cache_expired_at
    # )


def init_container(app):
    container = Container()
    container.config.from_dict(settings.model_dump())
    container.wire(
        modules=[
            "src.api.user.repository",
            "src.models.user",
        ]
    )
    app.container = container

    return app
