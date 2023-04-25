import mmap,os, time, signal

def handler_padre(s,f):
    pass

def handler_hijo(s,f):
    pass

memoria = mmap.mmap(-1, 100)

pid = os.fork()

if pid == 0:
    # hijo
    signal.signal(signal.SIGUSR2, handler_hijo)
    memoria.write(b"hola papa, esto lo escribo antes de morirme\n")
    os.kill(os.getppid(), signal.SIGUSR1)
    signal.pause()
    leido = memoria.readline()
    print("Hijo leyendo: ", leido.decode())
    exit()

#padre
signal.signal(signal.SIGUSR1, handler_padre)
signal.pause()
leido = memoria.readline()
print("Padre leyendo: ", leido.decode())

memoria.write(b"hola hijo, que tal\n")
os.kill(pid, signal.SIGUSR2)

os.wait()

