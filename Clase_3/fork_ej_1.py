import os


print('SOY EL PADRE (PID: %d)' % os.getpid())
print('--------------------------------')
try:
  ret = os.fork()
except OSError:
  print('ERROR AL CREAR EL HIJO')
  
print(ret)


if ret > 0:
  print('SOY EL PADRE (PID: %d )' % os.getpid())
  
elif ret == 0:
  print('SOY EL HIJO (PID: %d -- PPID: %d)' % (os.getpid(), os.getppid()))


