from multiprocessing import Process, Queue
import os, time

def f(q):
    q.put([42, None, 'hello', os.getppid(), os.getpid()])
    q.put("hijo escribiendo otro mensaje...")
    time.sleep(1)
    print("Hijo muriendo....")

if __name__ == '__main__':
    q = Queue()
    q.put("hola mundo")
    q.put("hola mundo2")

    p = Process(target=f, args=(q,))
    p.start()
    p.join()
    print("El contenido de la cola es:")
    for i in range(4):
        print(q.get())   
