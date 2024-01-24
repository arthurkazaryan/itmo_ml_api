from celery import signature
from celery.result import AsyncResult

from repository import ModelRepository

from schema.model_schema import ModelPredict
from services.base_service import BaseService


class ModelService(BaseService):
    def __init__(self, model_repository: ModelRepository):
        self.model_repository = model_repository
        super().__init__(model_repository)


    def predict(self, user_id: int, model_name: str, data: ModelPredict):
        task = signature(model_name, kwargs={
            "user_id": user_id,
            "n_days": data.n_days,
            "drug": data.drug.value,
            "age": data.age,
            "sex": data.sex.value,
            "ascites": data.ascites.value,
            "hepatomegaly": data.hepatomegaly.value,
            "spiders": data.spiders.value,
            "edema": data.edema.value,
            "bilirubin": data.bilirubin,
            "cholesterol": data.cholesterol,
            "albumin": data.albumin,
            "copper": data.copper,
            "alk_phos": data.alk_phos,
            "sgot": data.sgot,
            "tryglicerides": data.tryglicerides,
            "platelets": data.platelets,
            "prothrombin": data.prothrombin,
            "stage": data.stage
        }, queue=model_name).delay()

        launched_task = AsyncResult(str(task))
        self.model_repository.create_inference(user_id=user_id, task_uuid=str(task), status=launched_task.status)

        return {"task_id": str(task), "status": launched_task.status}

    def status(self, task_id: str):
        launched_task = AsyncResult(task_id)
        response = {"task_id": task_id, "status": launched_task.status}
        if launched_task.status == "SUCCESS":
            response["result"] = launched_task.result[1]

        return response
