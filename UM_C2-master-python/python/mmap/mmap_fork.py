import mmap,os, time, signal

def handler_padre(s,f):
    leido = memoria.readline()
    print("Padre leyendo: ", leido.decode())

def handler_hijo(s,f):
    leido = memoria.readline()
    print("Hijo leyendo: ", leido.decode())

memoria = mmap.mmap(-1, 100)

pid = os.fork()

if pid == 0:
    # hijo
    signal.signal(signal.SIGUSR2, handler_hijo)
    memoria.write(b"hola papa, esto lo escribo antes de morirme\n")
    os.kill(os.getppid(), signal.SIGUSR1)
    signal.pause()
    exit()

#padre
signal.signal(signal.SIGUSR1, handler_padre)
signal.pause()
memoria.write(b"hola hijo, que tal\n")
os.kill(pid, signal.SIGUSR2)

os.wait()

