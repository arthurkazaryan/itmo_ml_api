import json
from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session

from model.user import User, UserBalance
from model.predictors import Models


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        User.metadata.create_all(self._engine)
        UserBalance.metadata.create_all(self._engine)
        Models.metadata.create_all(self._engine)

        with open("model/fixtures/models.json") as f:
            with self.session() as s:
                for item in json.load(f):
                    s.merge(Models(**item))
                s.commit()

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
