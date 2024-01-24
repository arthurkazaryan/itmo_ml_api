from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.routes import routers as router_v1
from core.container import Container
from util.class_object import singleton
from core.config import app_settings as configs


@singleton
class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=configs.PROJECT_NAME,
            openapi_url=f"/v1/openapi.json",
            docs_url='/v1/docs',
        )

        # set db and container
        self.container = Container()
        self.db = self.container.db()
        self.db.create_database()

        # set cors
        if configs.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        self.app.include_router(router_v1, prefix='/v1')


app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container
