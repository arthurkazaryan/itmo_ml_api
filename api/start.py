from fastapi import FastAPI

from api.v1.routes import router as router_v1


app = FastAPI(openapi_url='/v1/openapi.json', docs_url='/v1/docs')

app.include_router(router_v1, prefix='/v1')
