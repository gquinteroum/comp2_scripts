from calc_config import app
import time
@app.task
def verificar():
    time.sleep(20)
    return "Todo Ok, dale palante"
