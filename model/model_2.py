import pickle
from pathlib import Path

from celery.signals import task_success, task_failure
from celery.utils.log import get_task_logger

from celery_app.worker import app
from model.utils import preprocess_input


celery_log = get_task_logger(__name__)
model = pickle.load(open(Path("model_2/random_forest.mdl"), 'rb'))


@app.task(name='random_forest', bind=True)
def random_forest(self, user_id: int, n_days: int, drug: str, age: int, sex: str, ascites: str, hepatomegaly: str,
                  spiders: str, edema: str, bilirubin: float, cholesterol: float, albumin: float, copper: float,
                  alk_phos: float, sgot: float, tryglicerides: float, platelets: float, prothrombin: float, stage: float):

    celery_log.info(f'Task started. User: {user_id}')
    # task_id = self.request.id
    array = preprocess_input(n_days, drug, age, sex, ascites, hepatomegaly,
            spiders, edema, bilirubin, cholesterol, albumin, copper,
            alk_phos, sgot, tryglicerides, platelets, prothrombin, stage)

    result = model.predict(array)[0]

    return user_id, result


@task_success.connect(sender=random_forest)
def reduce_limit(sender=None, **kwargs):
    user_id, *_ = kwargs['result']
    pass


@task_success.connect(sender=random_forest)
def change_status_success(sender=None, **kwargs):
    user_id, *_ = kwargs['result']
    sender.request.id
    pass


@task_failure.connect(sender=random_forest)
def change_status_failure(sender=None, **kwargs):
    user_id, *_ = kwargs['result']
    sender.request.id
    pass
