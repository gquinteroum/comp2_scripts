
from multiprocessing import Process, Pipe, current_process, parent_process

def f(r,w,nproc):
    print("nproc vale: %d" % nproc)
    if(nproc == 2):
        print("receptor")
        print("%d: proc %d recibiendo: %s" % (nproc, current_process().pid,r.recv()))
        r.send("_hello world")
    if(nproc == 1):
        print("emisor")
        w.send("proc %d enviando" % (current_process().pid))
        print(str(nproc) + w.recv())
    r.close()
    w.close()
    print("Proceso PID %d (%d) terminando..." % (current_process().pid, nproc))

if __name__ == '__main__':
    r, w = Pipe()
    print("padre: %d" %current_process().pid)
    p1 = Process(target=f, args=(r,w,1))
    p2 = Process(target=f, args=(r,w,2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Bye...")
