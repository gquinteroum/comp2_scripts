#!/usr/bin/python
import threading, time

balance = 0 

s_balance = threading.Semaphore(0)

def deposit(amount, l):
    global balance
    global s_balance
    time.sleep(5)
    print ("deposito")
    balance = balance + amount
    l.release()

    s_balance.acquire()
    # esperar a que esté la extraccion para leer el balance
    print("deposit balance: %d" % balance)

def extract(amount, l):
    global balance
    global s_balance
    l.acquire()
    print ("extraccion")
    balance = balance - amount
    print("extract balance: %d" % balance)
    s_balance.release()


if __name__ == "__main__":
    th = []
    lock = threading.Semaphore(0)
    th.append(threading.Thread(target=deposit, args=(30000,lock)))
    th[-1].start()
    th.append(threading.Thread(target=extract, args=(8000,lock)))
    th[-1].start()
    
    for i in th:
        i.join()

    print("Final balance: %d" % balance)
