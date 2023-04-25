#!/usr/bin/env python
import subprocess as sp
import time
import sys
import os


def usage(progname):
    print("\nUsage:\n\tpython3 %s nombre_funcion\n\n" % progname)
    os._exit(1)

if len(sys.argv)==1:
    usage(sys.argv[0])


"""
Ejecuta un "ls -l /" y su resultado lo muestra por pantalla
"""
def ej0():
    process = sp.Popen(["ls", "-l", "/"])


"""
se llama al comando ls
tanto stdout como stderr se direccionan al PIPE
communicate ejecuta el comando y devuelve las dos salidas en tupla
probar generar un error
"""
def ej1():
    process = sp.Popen(["ls", "-l", "/"], stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = process.communicate()
    print(stdout)
    print(stderr)


"""
si shell es true el comando se ejecutara en una shell, es recomendable pasarlo como string.
Si no, por default es false, hay que pasar la lista.
"""
def ej2():
    sp.Popen(["ps", "fax"])
    time.sleep(1)
    print("-----------------------------------------------------")
    sp.Popen(["ps fax"], shell=True)
#    sp.Popen(["ls", "-l"])
#    sp.Popen(["ls -l"], shell=True)

"""
abre un archivo
ejecuta un comando y usa al archivo como salida estandar
"""
def ej3():
    fd = open("/tmp/file", "w+")
    fde = open("/tmp/filee", "w+")
    sp.Popen(["ip", "asfdaf"], stdout=fd, stderr=fde)

"""
carga un comando como "proc" usando stdout a pipe, y luego lee su contenido
"""
def ej4():
    with sp.Popen(["ip", "a"], stdout=sp.PIPE) as proc:
        print(proc.stdout.read())


# creo un proc hijo con popen y el padre espera con wait
def ej5():
    fin=sp.Popen(["sleep", "3"])
    fin.wait()
    print("terminando...")


# idem, pero el padre espera mientras no termina
# poll() retorna None mientras está en ejecucion, cuando termina, retorna el returncode
# cuando termina, poll() setea el returncode de la instancia Popen (fin en este caso)
def ej6():
    fin=sp.Popen(["sleep", "3"])
    while fin.poll() == None:
        print("Esperando a que termine...")
        time.sleep(1)
    print("terminando...")



#ver el out al communicate con un file como in
def ej7():
    fd = open("/tmp/test","r")
    fin = sp.Popen(["cat"], stdin=fd, stdout=sp.PIPE)
    print(fin.communicate()[0])


# ver el out en el communicate en base a un in como pipe
def ej8():
    fin = sp.Popen(["cat"], stdin=sp.PIPE, stdout=sp.PIPE)
    fin.stdin.write(b"hola")
    print(fin.communicate())


"""
ejecuta un proceso y el resultado va por pipe al segundo
el universal_newlines respeta los saltos de linea
"""
def ej9():
    p1 = sp.Popen(["ip", "a"],stdout=sp.PIPE)
    p2 = sp.Popen(["grep", "inet"],stdin=p1.stdout,stdout=sp.PIPE,stderr=sp.PIPE)
    p1.stdout.close()
    out, err = p2.communicate()

    print(out)

#usamos Popen para hacer ping, retorna un objeto Popen que leemos
def ej10():
    salida = sp.Popen(["ping", "-c 4", "1.1.1.1"], stdout=sp.PIPE, universal_newlines=True)
    salida.wait()
    print("este es el proceso padre...")
    print(salida.communicate()[0])

#ahora usamos call, bloqueante, retorna un codigo de terminacion
def ej11():
    salida = sp.Popen(["ping", "-c 4", "google.com"], stdout=sp.PIPE, universal_newlines=True)
    #salida = sp.call(["ping", "-c 4", "google.com"], stdout=sp.PIPE, universal_newlines=True)
    salida.wait()
    print("este es el proceso padre...")
    print(salida)

#por ultimo usamos check_out, bloqueante, retorna salida del comando
def ej12():
    s = sp.check_output(["ping", "-c 4", "google.com"])
    output = s.decode("utf-8")
 
    lines = output.split('\n')
 
    for line in lines:
        print(line)

def ej13():
    # subprocess.run
    """
    retorna un obj de tipo CompletedProcdess
    no captura la salida
    returncode tiene el valor de retorno del comando
    """
    resultado = sp.call(["sleep","5"])
    print(resultado)

funcion = sys.argv[1]
print("========================================== Ejecutando %s" % funcion)
globals()[funcion]()
