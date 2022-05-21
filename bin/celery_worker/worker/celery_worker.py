from celery import Celery

CeleryWorker = Celery('tasks', broker='pyamqp://guest:guest@rabbitmq//')

