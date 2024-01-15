from core.config import app_settings

# import databases
from sqlalchemy import (
    create_engine, MetaData, Table, Column,
    String, Integer, Boolean, Text, ForeignKey, LargeBinary, DateTime
)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


# def create_database(database_url: str):
#     database = databases.Database(database_url)
#     return database


# def init_models():
#     # from . import models
#     Base.metadata.create_all(engine)
#     # with open("db/models/fixtures/init_products.json") as f:
#     #     with session() as s:
#     #         for item in json.load(f):
#     #             s.merge(models.user.Product(**item))
#     #         s.commit()
#
# engine = create_engine(
#     str(app_settings.DATABASE_URL),
#     connect_args={"check_same_thread": False}
# )
# session = scoped_session(sessionmaker(
#     autocommit=False, autoflush=False, bind=engine
# ))
# Base = declarative_base()
# db = create_database(str(app_settings.DATABASE_URL))
