from dependency_injector import containers, providers

from core.config import app_settings as configs
from core.database import Database
from repository import *
from services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "api.v1.endpoints.auth",
            "api.v1.endpoints.model",
            "core.dependencies",
        ]
    )

    config = providers.Configuration()

    db = providers.Singleton(Database, db_url=str(configs.DATABASE_URL))

    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)
    model_repository = providers.Factory(ModelRepository, session_factory=db.provided.session)

    user_service = providers.Factory(UserService, user_repository=user_repository)

    auth_service = providers.Factory(AuthService, user_repository=user_repository)

    model_service = providers.Factory(ModelService, model_repository=model_repository)
