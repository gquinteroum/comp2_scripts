import threading

num = 0
lock = threading.Lock()

# print("un acquire")
# lock.acquire()
# num += 1
# print("otro acquire")
# lock.acquire() # Esto se bloqueará
# num += 2
# lock.release()

# Con RLock, no se bloquea
lock = threading.RLock()

print("un acquire")
lock.acquire()
num += 3
print("otro acquire")
lock.acquire() # Acá no se bloquea
num += 4
lock.release()
lock.release() # se debe llamar a release por cada acquire.
print(num)
