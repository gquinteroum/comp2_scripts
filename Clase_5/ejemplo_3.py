import os
import sys
import time

r,w = os.pipe()
pid = os.fork()

if pid:
    os.close(w)
    r = os.fdopen(r)

    print('P: leyendo...')
    while True:
        line = r.readline()

        if line:
            print('P: ', line)
        else:
            os.wait()
            print('P: FIN')
            exit()

else:
    os.close(r)
    w = os.fdopen(w, 'w')

    print('H: escribiendo...')
    
    for line in sys.stdin:
        w.write('%s' % line)
        w.flush()

    print('EOF en sdtin')
    w.close()
    time.sleep(3)
    print('H: FIN')



