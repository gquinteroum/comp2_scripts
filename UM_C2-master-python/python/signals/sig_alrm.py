#!/usr/bin/python
import signal, os, time

#def handler(signum, frame):
#    print('Signal handler called with signal', signum)

def handler(s, f):
    print('Signal handler called with signal')
    signal.alarm(1)


def main():
    signal.signal(signal.SIGALRM, handler)

    print("Antes del alarm")
    signal.alarm(1)
    print("Despues del alarm, antes del pause")
    #signal.pause()
    print("esperando....")
    time.sleep(10)
    print("Despues del pause")
    
    #signal.alarm(0)          # Disable the alarm

if __name__ == "__main__":
    main()

