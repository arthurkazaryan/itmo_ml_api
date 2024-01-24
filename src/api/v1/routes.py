from fastapi import APIRouter

from api.v1.endpoints.auth import router as auth_router
from api.v1.endpoints.model import router as model_router


routers = APIRouter()
router_list = [auth_router, model_router]

for router in router_list:
    routers.include_router(router)
