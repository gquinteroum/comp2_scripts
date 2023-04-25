
from celery import Celery

app = Celery('calc', broker='redis://localhost:6379', backend='redis://localhost:6379', include=['calc', 'mensajes'])


