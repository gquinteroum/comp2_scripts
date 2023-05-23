import threading as th
import multiprocessing as mp
import os


def square(x):
    print('PID ', os.getpid())
    print('R: ', x**2)
    

print('PID PADRE', os.getpid())
p = mp.Process(target=square, args=(4,))
p.start()
p.join()

t = th.Thread(target=square, args=(4,))
t.start()
t.join()
