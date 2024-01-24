from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from core.exceptions import DuplicatedError
from model.predictors import Inference
from repository.base_repository import BaseRepository


class ModelRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Inference)


    def create_inference(self, user_id: int, task_uuid: str, status: str):

        with self.session_factory() as session:
            query = self.model(user_id=user_id, task_uuid=task_uuid, status=status)
            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                raise DuplicatedError(detail=str(e.orig))
            return query
