from model.predictors import Inference
from model.user import User


async def create_inference(s, user_id: int, task_uuid: str, status: str):
    inference = s.merge(Inference(user_id=user_id, task_uuid=task_uuid, status=status))
    s.commit()
    return inference


async def update_inference(s, task_uuid: str, status: str):
    inference = s.query(Inference).filter_by(task_uuid=task_uuid).one_or_none()
    if inference:
        inference.status = status
        s.commit()
    return inference


async def decrease_balance(s, user_id: int):

    user = s.query(User).filter_by(id=user_id).one_or_none()
    if user:
        user.balance -= 1
        s.commit()
    return user
