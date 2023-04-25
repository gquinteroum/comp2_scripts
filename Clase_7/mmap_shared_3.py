import mmap
import os
import time


area = mmap.mmap(-1, 16)

pid = os.fork()

if pid == 0:
    area.write(b'soy el hijo')
    area.seek(0)
    time.sleep(2)
    print(area.read(16))
    exit()

time.sleep(1)
leido = area.read(16)
area.seek(0)
area.write(leido.decode().upper().encode())
os.wait()
