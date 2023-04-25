#!/usr/bin/python

from os import fork
import time

def main():
    # es como si hicieramos esto:
    ret = fork()
    # -------------------------------------------------------
    # desde acá lo ejecutan los dos procesos "a la vez"
    if ret == 0:
        print("Hola desde el hijo!")
    else:
        time.sleep(0.001)
        print("Hola desde el padre!")


if __name__ == "__main__":
    main()
