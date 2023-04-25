import os, time, sys


pipe_name = '/tmp/pipe_test'

def lector( ):
    pipein = open(pipe_name, "r")
    for line in pipein:
        #line = os.read(pipein)
        print('Parent %d got "%s" at %s' % (os.getpid(), line[:-1], time.time( )))

# inicio del codigo
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)  


lector()
