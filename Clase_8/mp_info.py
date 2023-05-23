from multiprocessing import Process
import os, time

def child1():
    print("Child 1",os.getpid())

def child2():
    print("Child 2",os.getpid())
    print("hijo trabajando....")
    time.sleep(4)


if __name__=="__main__":
   print("Parent ID",os.getpid())
   # se crean los procesos (no se ejecutan)
   p1=Process(target=child1)
   p2=Process(target=child2)

   # se ejecutan los procesos (hace fork internamente)
   p1.start()
   p2.start()

   # todo esto lo hace el padre
   # ident es un atributo del objeto Process
   print("PID p1: %d" % p1.ident)
   print("PID p2: %d" % p2.pid)
#   os.kill(p1.ident, signal.asdfas)

   # join() e is_alive() son metodos del objeto Process
   p1.join()
   alive='Yes' if p1.is_alive() else 'No'
   print("Is p1 alive?",alive)
   time.sleep(1)
   #os.system("ps fax")
   alive='Yes' if p2.is_alive() else 'No'
   print("Is p2 alive?",alive)
#   p2.kill() # envia el SIGKILL al proceso
#   p2.terminate() # envia el SIGTERM al proceso
   p2.join()
   print("We're done")
