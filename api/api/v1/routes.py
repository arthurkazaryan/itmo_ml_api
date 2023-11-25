from fastapi import APIRouter

from api.v1.endpoints.index import router as index_router

routers = APIRouter()
router_list = [index_router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
