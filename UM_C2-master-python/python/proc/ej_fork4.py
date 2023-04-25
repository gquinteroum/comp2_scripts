#!/usr/bin/python

from os import fork, getpid
import time

"""
fork retorna:
    0 en el proceso hijo
    pid_hijo en el proceso padre

    fork() or fork()
    
    genera un proc hijo con el 1er fork
    ese fork retorna:
        en el padre: pid hijo (True)
            al ser True no requiere ejecutar nada mas: sabe que el OR es True
        en el hijo: 0 (False)
            al ser False, no sabe el resultado final del OR, debe evaluar la otra parte
            este hijo recibe un pid_hijo (True)
            el nuevo hijo recibe 0 (False)
"""

def main():
    #fork()
    fork() or fork() 

    print("Forkeando!!", getpid())
    time.sleep(100)


if __name__ == "__main__":
    main()














