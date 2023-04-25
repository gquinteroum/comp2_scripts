import os, mmap, sys, signal
from multiprocessing import Process

def f1():
    filename = sys.argv[1]
    content = sys.argv[2]

    filesize = 100

    # abrimos el archivo en alto nivel (sin OS)
    fd = open(filename, "w+")

    print(f"fileno: {fd.fileno()}")

    # fija un tamaño del archivo a filesize
    # si el archivo es mas grande lo trunca
    # si el archivo es mas chico, lo "estira" a ese tamaño
    os.ftruncate(fd.fileno(), filesize)

    # creamos un bloque en memoria RAM, referenciado por "mem"
    # y asociado/enlazado al archivo abierto
    mem = mmap.mmap(fd.fileno(), filesize)

    # escribimos en el bloque de memoria mapeada
    mem.write(bytes(content+"\n", "utf-8"))

    # volcamos el buffer de escritura a la memoria mapeada
    mem.flush()

    # cerramos la memoria (desmapea el archivo)
    mem.close()

    # cerramos el archivo
    fd.close()

def f2():
    content = sys.argv[1]

    filesize = 100

    # creamos un bloque en memoria RAM, referenciado por "mem"
    mem = mmap.mmap(-1, filesize)

    # escribimos en el bloque de memoria mapeada
    mem.write(bytes(content+"\n", "utf-8"))

    # volcamos el buffer de escritura a la memoria mapeada
    mem.flush()

    # leer el contenido de la memoria mapeada
    # rebobonar el segmento de memoria mapeada
    mem.seek(0)
    print("Contenido de mem: " + mem.read().decode())

    # cerramos la memoria (desmapea el archivo)
    mem.close()


def hijo(m):
    m.write(b"soy el hijo...\n")


def f3():

    mem = mmap.mmap(-1, 100)

    p = Process(target=hijo, args=(mem,))
    p.start()
    p.join()
    leido = mem.readline().decode()
    print("Padre lee: %s" % leido )

f3()


"""
    mmap.mmap(filedescr, size)
        filedescr = para memoria anonima local, -1
            para mapear un file en memoria se abre el archivo, y se pasa a mmap el fd.fileno()
        size: en bytes
        flags=MAP_PRIVATE|(MAP_SHARED)
        prot=PROT_WRITE|PROT_READ (default ambos)
"""
