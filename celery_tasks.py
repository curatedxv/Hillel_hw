import os

from celery import Celery

app = Celery('tasks', broker=f'pyamqp://guest@{os.environ.get("RABBITMQ_HOST", "localhost")}//')

@app.task
def add(x, y):
    print(x+y)