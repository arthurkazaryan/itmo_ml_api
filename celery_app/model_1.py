import pickle
from pathlib import Path

from celery.signals import task_success, task_failure
from celery.utils.log import get_task_logger

from celery_app.worker import app
from celery_app.utils import preprocess_input


celery_log = get_task_logger(__name__)
model = pickle.load(open(Path("celery_app/dump/model_1/log_reg.mdl"), 'rb'))


@app.task(name='model_1')
def model_1(user_id: int, n_days: int, drug: str, age: int, sex: str, ascites: str, hepatomegaly: str,
            spiders: str, edema: str, bilirubin: float, cholesterol: float, albumin: float, copper: float,
            alk_phos: float, sgot: float, tryglicerides: float, platelets: float, prothrombin: float, stage: float):

    celery_log.info(f'Task started. User: {user_id}')
    array = preprocess_input(n_days, drug, age, sex, ascites, hepatomegaly,
            spiders, edema, bilirubin, cholesterol, albumin, copper,
            alk_phos, sgot, tryglicerides, platelets, prothrombin, stage)
    result = model.predict(array)[0]

    return user_id, int(result)


@task_success.connect(sender=model_1)
def reduce_limit(sender=None, **kwargs):
    pass


@task_success.connect(sender=model_1)
def change_status_success(sender=None, **kwargs):
    user_id, class_id = kwargs['result']
    pass


@task_failure.connect(sender=model_1)
def change_status_failure(sender=None, **kwargs):
    pass
