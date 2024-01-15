from multiprocessing import cpu_count
from os import environ

from core.config import app_settings


bind = '0.0.0.0:' + str(app_settings.API_PORT)
workers = environ.get('WORKERS', cpu_count())
worker_class = 'uvicorn.workers.UvicornWorker'
timeout = 30

accesslog = '/dev/stdout'
access_log_format = '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
