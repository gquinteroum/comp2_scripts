import os
import signal

def handler(s, f):
    print('Llegó la señal ', s)
    print(f)


# signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGINT, handler)

input()
