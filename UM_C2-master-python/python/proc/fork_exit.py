import os, time


def f_hijo():
    print("hijo: mi pid es: %d, soy hijo de %d" % (os.getpid(), os.getppid()))
    for i in range(2):
        print("Hijo procesando... "+str(i))
        time.sleep(1)
    os._exit(0)
    """
    os._exit() llama al _exit() de posix, 
    mientras que sys.exit() termina normalmente el programa python
        esto permite también que la ejecución vuelva al programa anterior (como un return)
        es igual a SystemExit() que sale del intérprete python
    """

pid = os.fork()

if pid==0:
    f_hijo()


print("padre esperando... soy %d" % os.getpid())
pid,estado = os.wait()
print("Padre terminando... termino %d con %d" % (pid,estado))


