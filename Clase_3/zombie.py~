import os, time

pid = os.fork()

if pid == 0:
  os.execlp("sleep", "sleep", "5")

time.sleep(10)  
print('Finalizando el padre')

