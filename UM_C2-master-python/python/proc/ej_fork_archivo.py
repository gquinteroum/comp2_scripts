#!/usr/bin/python

from os import fork, getpid
import time
import sys

def main():
    fd = open("/tmp/archivo.txt", "w+")

    if fork() == 0:
        # esto lo ejecuta el proc hijo
        print("esto va en el hijo: ", getpid())
        fd.write("hola mundo desde el hijo: ")
        fd.flush()

    else:
        # esto lo ejecuta el proc padre
        print("esto va en el padre: ", getpid())
        time.sleep(1)
        fd.seek(0)
        print(fd.read())

    time.sleep(200)

if __name__ == "__main__":
    main()
