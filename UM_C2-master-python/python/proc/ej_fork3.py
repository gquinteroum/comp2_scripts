#!/usr/bin/python

from os import fork
import time

def main():
    numero = 1
    if fork() == 0:
        # esto lo ejecuta el proc hijo
        numero += 1
        print("Numero en el hijo tiene %d" % numero)
    else:
        # esto lo ejecuta el proc padre
        time.sleep(0.01)
        numero -= 1
        print("Numero en el padre tiene %d" % numero)


if __name__ == "__main__":
    main()
