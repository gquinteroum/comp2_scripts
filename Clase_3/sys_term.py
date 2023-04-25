import sys
import time


for i in range(10):
    sys.stdout.write("\033[0;35m+")
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\n")
