
import os, mmap, sys

filesize=100

mem = mmap.mmap(-1, filesize)

mem.write(b"hola mundo\n")
mem.flush()

mem.seek(0)
print(mem.read().decode())
mem.close()
