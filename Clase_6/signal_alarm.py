import os, signal
import time

def handler(s, f):
    print('Se ha llamado al manejador')
    # print(f)

def main():
    signal.signal(signal.SIGALRM, handler)

    print("Antes de alarm")
    signal.alarm(5)
    print("Después de alarm y antes de pause")
    signal.pause()
    # time.sleep(10)
    print("Después de pause")

    signal.alarm(0)  #Deshabilita la alarma

if __name__ == '__main__':
    main()


    
