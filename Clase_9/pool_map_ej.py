from multiprocessing import Process, Pool
import time
import os

# fifo_name = '/tmp/pool_fifo'

def foo(t):
    time.sleep(t)
    print('H: ' + str(os.getpid()) + ' ' + str(t))
#    fifo = open(fifo_name, 'w')
#    fifo.write('H: ' + str(os.getpid()) + ' ' + str(t))
#    fifo.flush()
#    fifo.close()
    return t
    
    

pool = Pool(processes=4)

# result =  pool.map(foo, [0,1,2,3,4,5,6])
# print('FIN')
result = pool.map_async(foo, [0,1,2,3])#,4,5,6])
# print(result)

for i in range(10):
    time.sleep(1)
    print('P: ', i)

print(result.get(timeout=0))
print('FIN')


