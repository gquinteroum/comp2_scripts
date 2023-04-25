import mmap
import os

# Se define la longitud de la región de memoria a asignar
# mem_size = os.sysconf('SC_PAGE_SIZE') * 10
mem_size = 64
# Se crea un objeto mmap que representa la región de memoria mapeada
mem = mmap.mmap(-1, mem_size, mmap.MAP_ANONYMOUS | mmap.MAP_SHARED)

# Se escribe en la región de memoria compartida
mem.write(b'Hola, esta es una prueba de memoria compartida.')

# Se lee de la región de memoria compartida
mem.seek(0)
data = mem.read(mem_size)

print(data)

# Se libera la región de memoria compartida
mem.close()

