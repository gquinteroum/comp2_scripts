#reading stdin from subprocess / multiprocessing
# starting a child process closes standard file descriptors
# to use them, you need re-open 

import sys,multiprocessing

def func():
    sys.stdin = open(0)
#    print(sys.stdin)
    print("Ingrese una linea: ")
    c = sys.stdin.readline()
    print('Got', c)


multiprocessing.Process(target=func).start()
