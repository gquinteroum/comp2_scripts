from celery import Celery

app = Celery('celery_config', broker='redis://192.168.0.10:6379/0', backend='redis://192.168.0.10:6379', include=['url_celery'])
