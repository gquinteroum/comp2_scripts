
import os,time

pid = os.fork()

if not pid:
    print("soy el hijo")
    time.sleep(2)
    os.execlp("ls", "/usr/bin/ls", "-l")
    print("hijo saliendo")
else:
    print("soy el padre")
    os.wait()
    print("padre saliendo")

