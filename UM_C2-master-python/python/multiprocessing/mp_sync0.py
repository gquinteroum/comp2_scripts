import multiprocessing
import time
import mmap



def calculo(v):
    time.sleep(1)
    v.write(b"cambiando\n")

def resultado(valor):
    print("Valor: %s" % valor.readline().decode())





if __name__ == "__main__":
    valor = mmap.mmap(-1, 20)
    valor.write(b"nada\n")
    valor.flush()
    # p1 = multiprocessing.Process(target=calculo, args=(valor,))
    p2 = multiprocessing.Process(target=resultado, args=(valor,))
    # p1.start()
    p2.start()
    # p1.join()
    p2.join()
