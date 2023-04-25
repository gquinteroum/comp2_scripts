import os
import sys
import time



def main():
    
  fd = open('./archivo.txt', 'w+')
  
  
  pid = os.fork()

  if (pid): # Este es el proceso padre
    print('PADRE (PID: %d)' % os.getpid())
    time.sleep(1)
    fd.seek(0)
    print(fd.read())
    
  
  else: # Proceso hijo
    print('HIJO (PID: %d)' % os.getpid())
    fd.write('Esto es una línea del HIJO')
    fd.flush()
    
      
      
  time.sleep(60)

if __name__ == "__main__":
  main()
 