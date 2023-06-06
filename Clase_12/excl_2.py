import threading


# Variable compartida entre hilos
cont = 0
loop_amount = 1000000 #Incrementar la cantidad de incrementos y decrementos
lock = threading.Lock()

# Funcion que incrementa el contador de forma segura
def add(loop_amount):
    global cont
    for i in range(loop_amount):
        lock.acquire()
        cont = cont + 1
        lock.release()
        
def sub(loop_amount):
    global cont
    for i in range(loop_amount):
        lock.acquire()
        cont = cont - 1
        lock.release()

# Creamos dos hilos que incrementan y decrementan el contador
t1 = threading.Thread(target=add, args=(loop_amount,))
t2 = threading.Thread(target=sub, args=(loop_amount,))
t1.start()
t2.start()

# Esperamos a que todos los hilos terminen
t1.join()
t2.join()


# Imprimimos el resultado final
print "Resultado:\n", cont
