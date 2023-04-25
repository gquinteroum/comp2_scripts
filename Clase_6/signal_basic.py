from time import sleep
import signal, os

def funcionUSR2(s, frame):
    print("Recibiendo senal USR2 ", s)
    print("Frame:", frame)


def main():
    print("kill -USR2 ", os.getpid()) 
    
    # -9 -2 -USR1/2 -STOP 
    #sig stop y sig kill no pueden modificarse!
    signal.signal(signal.SIGUSR1, signal.SIG_IGN)
    signal.signal(signal.SIGUSR2, funcionUSR2)


    print("Señal 2: "    + str(signal.getsignal(signal.SIGINT)))
    print("Señal USR1: " + str(signal.getsignal(signal.SIGUSR1)))
    print("Señal USR2: " + str(signal.getsignal(signal.SIGUSR2)))
    print("Señal STOP: " + str(signal.getsignal(signal.SIGSTOP)))
    print("Señal KILL: " + str(signal.getsignal(signal.SIGKILL))) 
    
    sleep(1000)

    print("Saliendo")


if __name__ == '__main__':
    main()
