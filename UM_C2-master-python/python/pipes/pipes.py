import os, sys, time

def f0():
    r, w = os.pipe() 
    r = os.fdopen(r)
    w = os.fdopen(w, 'w')
    msg = input("Introduzca un mensaje:")
    w.write(msg)
    w.close()
    print("Mensaje leido: %s" % r.readline())
    r.close()



def f1():
    # file descriptors r, w for reading and writing
    r, w = os.pipe() 

    processid = os.fork()
    if processid:
        os.close(w)
        r = os.fdopen(r)
        print("Parent reading")
        cadena = r.readline()
        print("text = %s\n" % cadena)
        os.wait()
        sys.exit(0)

    else:
        # This is the child process
        os.close(r)
        w = os.fdopen(w, 'w')
        # w es un obj archivo abierto conectado con el fd w
        print("Child writing")
        w.write("Text written by child...\n esto va al limbo\n")
        w.close()
        print("Child closing")
        sys.exit(0)


def f2():
    r,w = os.pipe()
    pid = os.fork()
    if pid:
        os.close(w)
        r = os.fdopen(r)
        print("padre leyendo...")
        while True:
            line = r.readline()
            if line:
                print("Padre leyendo: %s" % line)
            else:
                os.wait()
                print("Terminando padre...")
                sys.exit(0)
    else:
        os.close(r)
        w = os.fdopen(w,'w')
        print("Hijo escribiendo...")
        for line in sys.stdin:
            w.write("%s" % line)
            w.flush()
        print("Encontrado EOF en el stdin...")
        w.close()
        time.sleep(3)
        print("Hijo terminando...")
        ### otras 10mil lineas
            
    

f0()
