import signal, os, time

def handler(signum, frame):
    print('Mmmmm... no me estoy muriendo creo...'+str(signum)+"-"+ str(frame)+"\n")
    signal.signal(signal.SIGINT, signal.SIG_DFL)

print(signal.getsignal(signal.SIGINT))
# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGINT, handler)

print(signal.getsignal(signal.SIGINT))

time.sleep(100)

