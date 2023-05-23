from multiprocessing import Process, Pipe
import time

def f(child_conn):
    child_conn.send([42, None, 'hello'])
    print("H: Hijo recibiendo: " + child_conn.recv())
    child_conn.send("hola mundo")
    print("H: " + child_conn.recv())
    child_conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print ("P: " + str(parent_conn.recv()))   # prints "[42, None, 'hello']"
    parent_conn.send("enviando desde el padre...")
    for i in range(5):
        print("Padre haciendo cosas de padre...")
        time.sleep(1)

    print ("P: " + parent_conn.recv())
    parent_conn.send("hola")
    p.join()
