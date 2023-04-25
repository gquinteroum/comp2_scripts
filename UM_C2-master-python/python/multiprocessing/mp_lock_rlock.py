import multiprocessing, time

def bajo(l):
    for i in range(5):
        l.acquire()
        print("Bajando el lock...")
    time.sleep(100)

def subo(l):
    for i in range(5):
        print("Subiendo el lock...")
        time.sleep(1)
        l.release()




if __name__ == "__main__":
    l = multiprocessing.Lock()

    multiprocessing.Process(target=bajo, args=(l,)).start()
    multiprocessing.Process(target=subo, args=(l,)).start()

    # probar con RLock()
