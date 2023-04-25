import os
import sys
import time



def main():
    
  fd = open('./archivo.txt', 'w+')
  
  
  pid = os.fork()

  if (pid): # Este es el proceso padre
    print('PADRE (PID: %d)' % os.getpid())
    time.sleep(1)
#      fd.seek(0)
    print(fd.read())
    
#    fd.write('Esto es una línea del PADRE')
#    fd.flush() #Cuando se escribe en un archivo se escribe sobre un buffer. Para que el contenido del buffer sea escrito en el archivo se debe usar flush o cerrar el archivo o terminar el proceso correctamente
  
  else: # Proceso hijo
    print('HIJO (PID: %d)' % os.getpid())
    fd.write('Esto es una línea del HIJO')
    fd.flush()
    sys.exit(0)
      
      
#  time.sleep(60) # Los files descriptors se comparten. Por ese motivo ambos pueden ver lo que esta pasando en el archivo. sudo ls -l /proc/pid/fd

if __name__ == "__main__":
  main()
 

