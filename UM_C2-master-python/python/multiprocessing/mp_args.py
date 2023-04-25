
import os
from multiprocessing import Process
# import multiprocessing as mp

def testing():
    print("Works")

def square(n):
    print(f"The number {n} squares to {n**2}")

def cube(n):
    print(f"The number {n} cubes to {n**3}")

def multip(n,m):
    print(f"The product of {n} and {m} is: {n*m}")

if __name__=="__main__":

    p = []
    p.append(Process(target=square,args=[7,]))
    p.append(Process(target=cube,args=(3,)))
    p.append(Process(target=testing))
    p.append(Process(target=multip,args=(4,5)))

#    for i in range(4):
#        p[i].start()

    os.system("ps ft")
    for i in range(4):
        print(p[i].is_alive())
    os.system("ps ft")

    for i in range(4):
        p[i].join()

    for i in range(4):
        print(p[i].is_alive())
    print("We're done")
