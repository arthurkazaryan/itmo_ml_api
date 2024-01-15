from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse


router = APIRouter(
    prefix="/index",
    tags=["index"],
)


@router.get("/")
async def index():
    return JSONResponse(content={"status": "ok"}, status_code=200)
