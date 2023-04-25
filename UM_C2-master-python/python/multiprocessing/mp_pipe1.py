from multiprocessing import Process, Pipe
import time

def f(conn):
    conn.send("Mensaje 1")
    conn.send("Mensaje 2")
    conn.close()
    print("Labor completada, a morir...")

if __name__ == '__main__':
    a, b = Pipe()
    p = Process(target=f, args=(b,))
    p.start()
    time.sleep(2)
    print ("Padre 1: " + str(a.recv())) 
    print ("Padre 2: " + str(a.recv())) 
    print ("Padre 3: " + str(a.recv())) 

    p.join()
    print("Hora de morir tambien... Bye... (x.x)")
