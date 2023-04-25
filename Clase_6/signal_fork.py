import os, time, signal

def handler_padre(s, f):
    print("Padre - PID: %d (PPID: %d) " % (os.getpid(), os.getppid()))

def handler_hijo(s, f):
    print("Hijo - PID: %d (PPID: %d) " % (os.getpid(), os.getppid()))


"""
Enviarle al padre y al hijo, una señal USR1
"""

def hijo():
    print('Iniciando hijo PID: ', os.getpid())

    while True:
        print('Hijo en espera')
        signal.pause()

def main():
    pid = os.fork()

    if pid == 0:
        signal.signal(signal.SIGUSR1, handler_hijo)
        hijo()
    else:
         signal.signal(signal.SIGUSR1, handler_padre)
         print('Iniciando padre: ', os.getpid())

         for i in range(100):
             time.sleep(5)
             os.kill(pid, signal.SIGUSR1)
          
          
         print('Padre matando al hijo...')
         os.kill(pid, signal.SIGTERM)
         print('Padre terminando...')

if  __name__ == '__main__':
    main()


