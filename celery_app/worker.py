import os

from celery import Celery
from dotenv import load_dotenv

"""
Загрузка через load_dotenv вместо app_settings для Flower
"""

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")

app = Celery(
    'itmo_api',
    broker=REDIS_URL,
    backend=REDIS_URL,
)

app.conf.timezone = "Europe/Paris"
app.conf.task_track_started = True
