import os
import signal

"""
signal.SIG_IGN -> ignorar la señal
signal.SIG_DFL -> comportamiento por defecto
funcion(s, f)  -> handler a ejecutar
"""

def manejador_usr1(sig, frame):
    print("Manejando la señal ", sig)
    print("Frame: ", frame)
    
print(os.getpid())

print("Ignoramos la señal USR1")
signal.signal(signal.SIGUSR1, signal.SIG_IGN)
input()

print("Redefinimos la señal USR1: default")
signal.signal(signal.SIGUSR1, signal.SIG_DFL)
input()

print("Redefinimos la señal USR1: handler")
signal.signal(signal.SIGUSR1, manejador_usr1)
input()


