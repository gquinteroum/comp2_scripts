import os
import time 


r, w = os.pipe()

#os.close(r)
while True:
    leido = os.read(0, 512)
    if len(leido) == 0:
        break

    os.write(w, leido)
    #time.sleep(1)
    leido = os.read(r, 512)
    if len(leido) == 0:
        break

    print('Luego del pipe: ', leido)


