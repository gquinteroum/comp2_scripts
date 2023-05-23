import sys
import threading
import time
import os


DELAY=10
ESPERAR=True

def thread_function(name):
    print("HILO: Iniciando hilo %s____________________________________________ mi PID es %d, Thread %d" % (name, os.getpid(), threading.get_ident()))
    print("HILO: saliendo de compras...")
    time.sleep(DELAY)
    print("HILO: volviendo a casa!")


if __name__ == "__main__":

    print("MAIN: Iniciando programa principal, antes de crear el thread_______ mi PID es %d, thread %d" % (os.getpid(), threading.get_ident()))

    x = threading.Thread(target=thread_function, args=(1,), daemon=False) # thread detached
    
    print("MAIN: Programa principal, thread creado, antes de lanzarlo...")

    x.start()

    time.sleep(1)
    print("MAIN: Hilo... volviste? Estás ahí?")
    time.sleep(2)
    print("MAIN: Hola??")
    time.sleep(3)
    print("MAIN: Alguien??")
    time.sleep(3)
    
    if(ESPERAR):
        x.join()
        print("Ejecutar el ps en terminal...")
        time.sleep(10)
        print("MAIN: Qué bueno que volviste! Podemos morir juntos ahora xD")
    else:
        print("MAIN: Qué soledad! Mejor me muero...")
