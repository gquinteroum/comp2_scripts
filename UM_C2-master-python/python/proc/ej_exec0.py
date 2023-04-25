
import os,time

print("antes del exec")
time.sleep(2)
os.execlp("ls", "/usr/bin/ls", "-l")
print("despues del exec")
