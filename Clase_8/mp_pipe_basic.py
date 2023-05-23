from multiprocessing import Process, Pipe
import time

def f(conn):
    while True:
      msg = conn.recv()
      if msg == 'end':
        break
        
      print("H: " + msg.upper())
      
    
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    
    while True:
      msg = input()
      parent_conn.send(msg)
      if msg == 'end':
        break
      
    p.join()
