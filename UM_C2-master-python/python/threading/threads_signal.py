import threading, signal, os

pid_hilo = 0

def handler(s,f):
    print("Señal: ", threading.current_thread().name)

def f1():
    global pid_hilo
    pid_hilo = threading.get_native_id()
    print(threading.get_native_id())
    signal.pause()
    print("fin hilo")

if __name__ == "__main__":
    print(os.getpid())
    signal.signal(signal.SIGUSR1, handler)
    t1 = threading.Thread(target=f1)

    t1.start()
    print("mandando señal al hilo")
    os.kill(pid_hilo, signal.SIGINT)
    signal.pause()
    print("Fin main")
    # espera....
