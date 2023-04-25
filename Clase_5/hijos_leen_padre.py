import os
import time 


r, w = os.pipe()

pid = os.fork()

if not pid:
    gs_pid = os.fork()

    if not gs_pid:
        os.close(w)
        
        while True:
            leido = os.read(r, 512)
            if len(leido) == 0:
                break

            print('Hijo: ', leido.decode('utf-8'))

        exit(0)
    else:
        os.close(w)
        time.sleep(10)
        while True:
            leido = os.read(r, 512)
            if len(leido) == 0:
                break

            print('Nieto: ', leido.decode('utf-8'))

        exit(0)

else:
    os.close(r)
    while True:
        leido = os.read(0, 512)
        if len(leido) == 0:
            break

        os.write(w, leido)
        
        
