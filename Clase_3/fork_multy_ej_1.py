import os
import time

def main():
    os.fork()
    os.fork()
    print('Hola mundo')
    
#    time.sleep(120) #Para ver la gerarqía  o el while
#    while True:
#      pass

if __name__ == "__main__":
  main()
 

