
import os, mmap, sys

filename = sys.argv[1]
filesize=100

fd = open(filename, "w+")

os.ftruncate(fd.fileno(), filesize)

mem = mmap.mmap(fd.fileno(), filesize)

mem.write(b"hola mundo\n")
mem.flush()
mem.close()
fd.close()
