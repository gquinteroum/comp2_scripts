import os, time

fd = open("/tmp/a/archivito.txt", "w+")

if not os.fork():
    fd.write("hijo escribiendo")
    fd.flush()  # fuerzo el volcado de buffer
else:
    time.sleep(1)
    fd.seek(0)
    print("Padre leyendo: ", fd.read())
    
print("cerrando el archivo...")
fd.close()
