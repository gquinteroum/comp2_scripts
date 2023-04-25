
import signal
import os
import traceback

def handler(signum, frame):
    print(signum, frame)
    print("print stack frames:")
    traceback.print_stack(frame)

def demo(n):
    if n == 3:
        os.kill(os.getpid(), signal.SIGUSR1)
        return
    demo(n+1)

signal.signal(signal.SIGUSR1, handler)
demo(1)
print("saliendo...")
