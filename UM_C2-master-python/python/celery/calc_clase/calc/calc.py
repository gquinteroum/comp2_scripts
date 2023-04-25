
from calc_config import app

@app.task
def suma(a, b):
    return a+b

@app.task
def resta(a, b):
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
def pot(a,b):
    return a**b
