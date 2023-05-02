import os, mmap

mem = mmap.mmap(-1, 16)

pid = os.fork()

if not pid:
    #proceso hijo
    mem.write(b'Linea')
    print('Offset del hijo', mem.tell())
    exit()

os.wait()
print('Offset del padre', mem.tell())
