
import threading, queue
import time

q = queue.Queue()
#q = queue.LifoQueue()

def worker():
    while True:
        print("Hilo ciclando...")
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()
        if q.empty():
            break

# turn-on the worker thread
hilo = threading.Thread(target=worker, daemon=True)
hilo.start()

# send thirty task requests to the worker
for item in range(30):
    print(f'Putting item {item}')
    q.put(item)
#    time.sleep(1)
q.join()
print('All task requests sent\n', end='')
print(f"Queue empty? -> {q.empty()}")
# block until all tasks are done
hilo.join()
print(f"Queue empty? -> {q.empty()}")
print('All work completed')
