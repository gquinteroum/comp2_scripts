import os
import signal

print(os.getpid())

signal.signal(signal.SIGUSR1, signal.SIG_IGN)
input('Se están ignorando las señales USR1')
signal.signal(signal.SIGUSR1, signal.SIG_DFL)
print('El manejo de la señal USR1 es el que tiene por defecto')
input()
