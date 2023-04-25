"""
Se pueden ver los procesos con ps lf.
Para ver los procesos padre se pueden ver con ps ps
"""

from ctypes import c_int, addressof
import os
import sys
import time

print('SOY EL PADRE (PID: %d)' % os.getpid())
var = 'valor original'
print(var, id(var))
print('--------------------------------')
try:
  ret = os.fork()
except OSError:
  print('ERROR AL CREAR EL HIJO')
  

#while True:
if ret > 0:
    var = 'datos cambiados por el padre'
    time.sleep(1)
    print('SOY EL PADRE (PID: %d )' % os.getpid())
    print(var, id(var))

elif ret == 0:
    var = 'datos cambiados por el hijo'
    time.sleep(1)
    print('SOY EL HIJO (PID: %d -- PPID: %d)' % (os.getpid(), os.getppid()))
    print(var, id(var))
  
  #time.sleep(1)
  #print()
  


