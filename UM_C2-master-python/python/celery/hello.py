
from celery import Celery

app = Celery('hello', broker='redis://localhost', backend='redis://localhost:6379')

@app.task
def hello():
    return 'hello world'


if __name__ == '__main__':
    app.start()
