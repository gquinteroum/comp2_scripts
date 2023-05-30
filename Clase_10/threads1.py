import sys
import threading
import time
import os

"""
    Python threads:
        _thread
        threading trabaja un poco más "arriba", abstracción de _thread

    LWP - Light Weight Process - "proceso ligero"
"""


DELAY=3

def thread_function(name):
    # print("Iniciando hilo %s (%d)" % (name, threading.current_thread().ident))
    print('Native id del hilo secundario ',  threading.get_native_id())
    time.sleep(DELAY)
    print("Finalizando hilo %s, se acabó el tiempo (%s)" % (name, threading.current_thread().name))


if __name__ == "__main__":
    print('PID: ', os.getpid())
    print("Native id del hilo principal ",  threading.get_native_id())
    print("Iniciando programa principal (%s), antes de crear el thread" % threading.current_thread().name)

    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    
    print("Programa principal, thread creado, antes de lanzarlo...")

    x.start()

    print("Programa principal: thread lanzado!")

    print("Programa principal, terminando ¿?")

    # print("\n ==> Tiene %d segundos para abrir otra terminal y ejecutar \" ps -eLf | grep %s | grep -v grep \" " % (DELAY, sys.argv[0]))


    # x.join()
    # por qué no termina el hilo principal??
    print("Hilo principal muriendo... chau")
    x.join()
    # queda esperando la terminacion de los hilos
