import os, time, sys


pipe_name = '/tmp/pipe_test'

def escritor( ):
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
    while True:
        print("escribiendo....")
        os.write(pipeout, b'Number %03d\n' % counter)
        counter = (counter+1) % 5
        time.sleep(1)

# inicio del codigo
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)  

escritor()
