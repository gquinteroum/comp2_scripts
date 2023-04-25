
import os, random
from multiprocessing import Process,Pipe

def productor(conn):
    valor = random.randint(1,10)
    conn.send(valor)
    print("Valor [%d] enviado por el proceso %d" % (valor,os.getpid()))
    conn.close()
    #nunca olvidar el close()

def consumidor(conn):
    print("Valor [%d] recibido por el proceso %d" % (conn.recv(), os.getpid()))


if __name__ == '__main__':
    prod_conn, cons_conn = Pipe()
    cons = Process(target=consumidor, args=(cons_conn,))
    prod = Process(target=productor, args=(prod_conn,))

    cons.start()
    prod.start()

    cons.join()
    prod.join()

    print("Terminando...")
