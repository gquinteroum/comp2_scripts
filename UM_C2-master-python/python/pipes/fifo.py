import os, time, sys

"""
    FILE* fd = fopen("sadfasdf", "w+") // alto nivel
    int fd = open("asfdasdf", O_WRONLY) // bajo nivel
"""

pipe_name = '/tmp/pipe_test'

def child( ):
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
    while True:
        os.write(pipeout, b'Number %03d\n' % counter)
        counter = (counter+1) % 5
        time.sleep(1)


def child_v2( ):
    pipeout = open(pipe_name, 'w')
    counter = 0
    while True:
        pipeout.write("Number %05d\n" % counter)
        counter = (counter+1) % 5
        pipeout.flush()
        time.sleep(1)

def parent( ):
    pipein = open(pipe_name, 'r')
    time.sleep(10)
    while True:
        line = pipein.readline()[:-1]
        print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time( )))

# inicio del codigo
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)  


pid = os.fork()    

if pid != 0:
    parent()
else:       
    child_v2()
