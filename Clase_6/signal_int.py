import signal, os, time

def handler(s, f):
    print("Terminando... ")

    signal.signal(signal.SIGINT, signal.SIG_DFL)

print(signal.getsignal(signal.SIGINT))

signal.signal(signal.SIGINT, handler)

print(signal.getsignal(signal.SIGINT))

time.sleep(100)
