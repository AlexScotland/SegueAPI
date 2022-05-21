from worker.celery_worker import CeleryWorker as app

@app.task
def add(x,y):
    return x + y
