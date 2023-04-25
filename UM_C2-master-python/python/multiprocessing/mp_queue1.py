import multiprocessing

def evenno(numbers, q):
    for n in numbers:
        if n % 2 == 0:
            q.put(n)
    print("Terminando hijo...")
   
if __name__ == "__main__":
   q = multiprocessing.Queue()
   p = multiprocessing.Process(target=evenno, args=(range(10), q))
   p.start()
   p.join()
   while q:
       try:
            print(q.get(True, 3))
       except Exception as e:
           print("Nada en la cola... saliendo")
           break
