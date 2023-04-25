
from celery import Celery
import os, time

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost:6379')

@app.task
def add(x, y):
    time.sleep(5)
    return x + y

@app.task
def mipid():
    time.sleep(0.5)
    return os.getpid()

#if __name__ == "__main__":
#    app.start()
