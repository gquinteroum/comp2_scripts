from multiprocessing import Process
import mmap

def f(mem):
    mem.write(b"Escribiendo desde el hijo...\n")


if __name__ == '__main__':
    memoria = mmap.mmap(-1, 100)


    p = Process(target=f, args=(memoria,))
    p.start()
    p.join()
    leido = memoria.readline()
    print("Leido: %s" % leido)


"""
    mmap.mmap(filedescr, size)
        filedescr = para memoria anonima local, -1
            para mapear un file en memoria se abre el archivo, y se pasa a mmap el fd.fileno()
        size: en bytes
        flags=MAP_PRIVATE|(MAP_SHARED)
        prot=PROT_WRITE|PROT_READ (default ambos)
"""
