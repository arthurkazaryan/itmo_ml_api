from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from celery_app.worker import app
from core.container import Container
from core.dependencies import get_current_active_user
from schema.model_schema import ModelPredict, ModelResponse, ModelStatus
from schema.user_schema import User
from services import ModelService


router = APIRouter(
    prefix="/model",
    tags=["model"],
)


@router.post("/{model_name}/predict", status_code=201, response_model=ModelResponse, response_model_exclude_none=True)
@inject
async def model_predict(model_name: str, data: ModelPredict,
                        current_user: User = Depends(get_current_active_user),
                        service: ModelService = Depends(Provide[Container.model_service])
                        ):

    if model_name not in ["model_1", "model_2"]:
        raise HTTPException(status_code=404, detail="Model not found")

    return service.predict(user_id=current_user.id, model_name=model_name, data=data)


@router.get("/status", status_code=200, response_model=ModelResponse, response_model_exclude_none=True)
@inject
async def model_status(data: ModelStatus = Depends(), service: ModelService = Depends(Provide[Container.model_service])):
    return service.status(task_id=str(data.task_id))
