#!/usr/bin/python
import threading, time

balance = 0 
lock = threading.Lock()

def deposit(amount):
    time.sleep(1)
    print ("deposito")
    global balance
    balance = balance + amount
    print("balance: %d" % balance)
    lock.release()

def extract(amount):
    global balance
    lock.acquire()
    print ("extraccion")
    balance = balance - amount
    print("balance: %d" % balance)


if __name__ == "__main__":
    lock.acquire()
    th = []
    th.append(threading.Thread(target=deposit, args=(30000,)))
    th[-1].start()
    th.append(threading.Thread(target=extract, args=(8000,)))
    th[-1].start()
    
    for i in th:
        i.join()

    print("Final balance: %d" % balance)
