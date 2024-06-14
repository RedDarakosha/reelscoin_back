from dependency_injector import containers, providers

from src.core.settings import Settings, settings
from src.core.db import init_db_pool, acquire_conn


class Container(containers.DeclarativeContainer):
    # # wiring_config = containers.WiringConfiguration(
    # #     auto_wire=True
    # )

    config = providers.Configuration("config")

    pool = providers.Resource(init_db_pool, settings.db_settings)
    connection = providers.Resource(acquire_conn, pool)


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
