"""
El padre y el hijo tendran el mismo PID ya que el hijo se ejecuta modificando el binario del padre.

"""


import os



print('SOY EL PADRE (PID: %d)' % os.getpid())
os.execlp('python', 'python', './hijo.py')

print('DA IGUAL LO QUE SE EJECUTE EN ESTE PUNTO PORQUE EXEC MODIFICA EL BINARIO ACTUAL')
  


