
from calc_config import app

@app.task
def saludo():
    return "Todo ok, celery andando"
