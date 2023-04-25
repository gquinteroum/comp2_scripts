#!/usr/bin/python3
import os,time,signal

def handler_padre(s,f):
    print("Padre... mensaje... PID: %d (PPID %d" % (os.getpid(), os.getppid()))

def handler_hijo(s,f):
    print("Hijo... mensaje... PID: %d (PPID %d" % (os.getpid(),os.getppid()))
    os.kill(os.getppid(), signal.SIGUSR1)
    # eso para poder distinguirlos xD
    # lo voy a correr y desde otra terminal le voy a mandar el USR1 al padre y al hijo para que veamos.


def hijo():
    print("Iniciando hijo PID: %d" % os.getpid())
    while True:
        print("Hijo esperando...")
        signal.pause()


def main():
#    signal.signal(signal.SIGUSR1,handler)
    pid=os.fork()

    if pid == 0:
        signal.signal(signal.SIGUSR1, handler_hijo)
        hijo()
    else:
        signal.signal(signal.SIGUSR1, handler_padre)
        print("Iniciando padre PID: %d" % os.getpid())
        for item in range(100):
            time.sleep(5)
            os.kill(pid,signal.SIGUSR1)
        print("Padre matando al hijo...")
        os.kill(pid,signal.SIGTERM)
        print("Padre terminando...")


if __name__ == "__main__":
    main()
