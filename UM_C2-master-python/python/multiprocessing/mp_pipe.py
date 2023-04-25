from multiprocessing import Process, Pipe
import time

def f(conn):
    conn.send([42, None, 'hello'])
    print("H: Hijo recibiendo: "+conn.recv())
    conn.send("hola mundo")
    print("H: "+conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print ("P: "+str(parent_conn.recv()))   # prints "[42, None, 'hello']"
    parent_conn.send("enviando desde el padre...")
    for i in range(5):
        print("Padre haciendo cosas de padre...")
        time.sleep(1)

    print ("P: "+parent_conn.recv())
    parent_conn.send("hola")
    p.join()
