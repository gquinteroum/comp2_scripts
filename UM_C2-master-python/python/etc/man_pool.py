import os
import multiprocessing, threading, time, getopt, sys

def func(x):
    while True:
        print("<<<< %s leyendo..." % multiprocessing.current_process().name)
        dato = x.recv()
        if dato==404:
            print("<<<< Proc %s saliendo..." % multiprocessing.current_process().name)
            break
        print("<<<< %s recibiendo %s" % (multiprocessing.current_process().name,str(dato)))
        print("<<<< %s enviando ok" % multiprocessing.current_process().name)
        x.send("ok  %d (%s)" % (dato,multiprocessing.current_process().name))

def server(x, n, p):
    print(">>>>>>>>>> Server %s recibiendo lista %s" % (threading.current_thread().getName(), str(n)))
    time.sleep(0.01)
    for i in n:
        print(">>>> %s enviando %d" % (threading.current_thread().getName(), i))
        x.send(i)
        print(">>>> %s recibiendo: %s" % (threading.current_thread().getName() ,x.recv()))
        time.sleep(1)
    x.send(404)
    p.join()


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]


def usage(progname):
    print("\n\tpython3 %s -p <num_proc> -n <num_max>\n\n" % progname)
    sys.exit(2)


if __name__ == "__main__":

    n = 0
    nproc = 0

    print(len(sys.argv))
    if len(sys.argv) != 5:
        usage(sys.argv[0])

    (opt,arg) = getopt.getopt(sys.argv[1:], 'p:n:', ["nproc=", "max="])

    for (op,ar) in opt:
        if(op in ['-p', '--nproc']):
            nproc = int(ar)
        elif(op in ['-n', '--max']):
            n = int(ar)
        else:
            usage(sys.argv[0])


    x = list(range(n))
    partes = split_list(x, nproc)
    print("Partes: "+ str(partes))

    procs = []
    thr = []
    pipes = []


    for part in partes:
        a,b = multiprocessing.Pipe()
        p = multiprocessing.Process(target=func, args=(a,))
        p.start()
        thr.append(threading.Thread(target=server, args=(b,part, p)))
        thr[-1].start()

    for h in thr:
        h.join()

    print("Terminando...")
