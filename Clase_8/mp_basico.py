#import multiprocessing
from multiprocessing import Process
import os, time

def child1():
    print("Child 1: %d, parent: %d" % (os.getpid(), os.getppid()))
    print("esperando...")
    time.sleep(5)
    os.system("ps ft")
    print("hijo muriendo...")


if __name__=="__main__":
    print("Parent ID",os.getpid())
    # creamos el objeto proceso (Process), no se ejecuta todavía
    p1=Process(target=child1)
    # p1.run()
#    child1()
    input("seguimos...")
    print("========================================================")
    print("Parent ID",os.getpid())
    p1.start()
    for i in range(10):
        print("Padre esperando a que el hijo muera...")
        time.sleep(1)

    print("PS  del padre (hijo muerto) -------------------------")
    os.system("ps ft")
    print("Padre libera al hijo zombie con join (simil wait)")
    p1.join()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    os.system("ps ft")

    print("We're done")

    #p1.kill() # envia un SIG_KILL al p1
