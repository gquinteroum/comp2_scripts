import mmap
import os

area = mmap.mmap(-1, 16)

pid = os.fork()

if pid == 0:
    area.write(b'soy el hijo')
    exit()

os.wait() #Comentar esta línea
print(area.read(16))
