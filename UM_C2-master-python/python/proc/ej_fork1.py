#!/usr/bin/python

from os import fork,getpid
import time

def main():
    fork()
    fork()
    fork()
    print("hola mundo", getpid())

    for i in range(10000000000000):
        print(i)

if __name__ == "__main__":
    main()
