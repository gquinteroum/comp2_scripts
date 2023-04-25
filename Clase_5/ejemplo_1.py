import os

r,w = os.pipe()

r = os.fdopen(r)
w = os.fdopen(w, 'w')

msg = input('Ingrese un mensaje: ')

w.write(msg)
w.close()

print('Mensaje leido: ', r.readline())

r.close()
