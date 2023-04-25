import sys
import threading
import time

"""
    Python threads:
        _thread
        threading trabaja un poco más "arriba", abstracción de _thread

    LWP - Light Weight Process - "proceso ligero"
"""


DELAY=50

def thread_function(name):
    print("Iniciando hilo %s (%d)" % (name, threading.current_thread().ident))
    time.sleep(DELAY)
    print("Finalizando hilo %s, se acabó el tiempo (%s)" % (name, threading.current_thread().name))


if __name__ == "__main__":

    print("Iniciando programa principal (%s), antes de crear el thread" % threading.current_thread().name)

    x = threading.Thread(target=thread_function, args=(1,))
    
    print("Programa principal, thread creado, antes de lanzarlo...")

    x.start()

    print("Programa principal: thread lanzado!")

    print("Programa principal, terminando ¿?")

    print("\n ==> Tiene %d segundos para abrir otra terminal y ejecutar \" ps -eLf | grep %s | grep -v grep \" " % (DELAY, sys.argv[0]))


    #x.join()
    # por qué no termina el hilo principal??
    print("Hilo principal muriendo... chau")

    # queda esperando la terminacion de los hilos

