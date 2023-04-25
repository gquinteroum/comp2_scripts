import os, time, sys

r, w = os.pipe()

ret = os.fork()
if not ret:
    os.close(w)
    time.sleep(10)
    r = os.fdopen(r)
    while True:
        #leido = os.read(r, 100)
        leido= r.readline(5)
        print("Hijo Leido: ", leido.upper())

for i in sys.stdin:
    os.write(w, i.encode())

