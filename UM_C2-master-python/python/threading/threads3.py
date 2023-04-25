import sys
import threading
import time
import os


DELAY=3

def thread_function(name):
    print("HILO %d: Este es el hilo: %s (%d)" % (name, threading.current_thread().name, threading.current_thread().ident))
    time.sleep(name)
    print("HILO %d: terminando" % name)


if __name__ == "__main__":

    print("MAIN: Iniciando programa principal, antes de crear el thread_______ mi PID es %d (%d)" % (os.getpid(), threading.current_thread().ident))

    x1 = threading.Thread(target=thread_function, args=(1,), daemon=True) 
    x2 = threading.Thread(target=thread_function, args=(2,)) 
    
    x1.start()
    x2.start()
  
    print("MAIN: cantidad de threads activos: ", threading.active_count())
#    print("MAIN: Este es el hilo: %s (%d)" % (threading.current_thread().name(), threading.current_thread().ident))

    for i in threading.enumerate():
        print("Nombre: ", i.name, "(",i.ident,", Vivo?: ",i.is_alive(),", Daemon?:",i.daemon)

    # hilo principal esperando...
    time.sleep(1.5)
    print("Estado x1: ", x1.is_alive())
    x1.join()

    # por acá
    # termina
