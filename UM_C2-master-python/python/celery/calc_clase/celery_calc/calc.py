
from calc_config import app
import time

@app.task
def suma(a, b):
    return a+b

@app.task
def resta(a, b):
    time.sleep(10)
    return a-b

@app.task
def mult(a, b):
    return a*b

@app.task
def div(a, b):
    if b!=0:
        return a/b
    return 0

@app.task
def pot(a, b):
    return a**b

@app.task
def pot2(a,b):
    #    chain = fetch_page.s(url) | parse_page.s() | store_page_info.s(url)
    tarea = mult.s(1,a)
    for i in range(b-1):
        tarea = tarea | mult.s(a)
    return tarea()
