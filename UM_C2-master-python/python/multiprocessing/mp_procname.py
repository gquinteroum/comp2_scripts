from multiprocessing import Process, current_process, parent_process
import os

def child1():
    print(current_process().name + " - PID: " + str(current_process().pid))
    print(parent_process().name + " - PPID: " + str(parent_process().pid))

def child2():
    print(current_process().name + " - PID: " + str(os.getpid()))



if __name__=="__main__":
   print("Parent ID",os.getpid())
   p1=Process(target=child1,name='Cualquier cosa')
   p2=Process(target=child2)
   p1.start()
   p2.start()
   p1.join()
   p2.join()
   print("We're done")
