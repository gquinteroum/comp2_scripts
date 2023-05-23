from multiprocessing import Process, Value, Array
import time


def foo(n):
    n.acquire()
    for i in range(5):
        print('H: ', i)
        time.sleep(1)
    n.release()

n = Value('i')
p = Process(target=foo, args=(n,))

p.start()
time.sleep(1)
n.value = 10
print('P', n.value)
p.join()
