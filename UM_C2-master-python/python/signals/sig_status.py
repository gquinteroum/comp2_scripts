import os
import signal

"""
signal.SIG_IGN -> ignorar la señal
signal.SIG_DFL -> comportamiento por default
funcion(s, f)  -> ejecuta este handler
"""

def manejador_user(senial, frame):
    if senial == signal.SIGUSR1:
        print("manejando la señal %d" % senial)
        print("Frame: ", frame)
    elif senial == signal.SIGUSR2:
        print("***manejando la señal %d" % senial)
        print("Frame: ", frame)

print(os.getpid())

print("comportamiento seteado en USR1: ", signal.getsignal(signal.SIGUSR1))
print("ignoramos la senial USR1")
signal.signal(signal.SIGUSR1, signal.SIG_IGN)
print("comportamiento seteado en USR1: ", signal.getsignal(signal.SIGUSR1))
os.read(0, 100)

print("redefiniendo USR1: default")
signal.signal(signal.SIGUSR1, signal.SIG_DFL)
print("comportamiento seteado en USR1: ", signal.getsignal(signal.SIGUSR1))
os.read(0, 100)

print("redefiniendo USR1 a un handler")
signal.signal(signal.SIGUSR1, manejador_user)
signal.signal(signal.SIGUSR2, manejador_user)
print("comportamiento seteado en USR1: ", signal.getsignal(signal.SIGUSR1))
os.read(0, 100)
