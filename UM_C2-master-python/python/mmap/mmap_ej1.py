import os,mmap

# creamos un segmento de memoria anonima
print("creando memoria mapeada anonima")

if not os.fork():
    memoria = mmap.mmap(-1, 100)
    # hijo
else:
    memoria = mmap.mmap(-1, 100)


print("escribiendo en la memoria - ", memoria.tell())
memoria.write(b"hola mundo")
#memoria.flush()

print("rebobinando...")
memoria.seek(0)

print("leyendo desde la memoria: - ", memoria.tell())
print(memoria.read().decode())

print("cerrando la memoria - ", memoria.tell())
memoria.close()
