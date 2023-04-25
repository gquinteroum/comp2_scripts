from concurrent.futures import ProcessPoolExecutor
from time import sleep

def return_after_5_secs(message):
    sleep(5)
    return message

pool = ProcessPoolExecutor(3)

future = pool.submit(return_after_5_secs, ("hello"))
print(future.done())
sleep(5)
print(future.done())
print("Result: " + future.result())
