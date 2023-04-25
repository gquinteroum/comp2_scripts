import os
print("abiertos...")
os.system("ls /proc/%d/fd" % os.getpid())
