from multiprocessing import Process, Value, Array

"""
    ctypes:
    'i': int (ej, 1, 222, etc)
    'd': double (ej 0.0, 1.22, etc)
"""

def func(num):
    num.value = 222
    print("Num en func: %d" % num.value)

def func2(arr):
    for i in range(len(arr)):
        arr[i] = -arr[i]

if __name__ == "__main__":
    num = Value('i', 0)
    num.value = 111

    arr = Array('i', range(10))

    print("Num antes de llamar al proceso: %d" % num.value)

    p = Process(target=func, args=(num,))
    p.start()
    p.join()
    print("Num en main: %d" % num.value)


    print("Arr en main (antes del proceso): " + str(arr[:]))
    p = Process(target=func2, args=(arr,))
    p.start()
    p.join()
    print("Arr en main: " + str(arr[:]))


