import sys, os


print('PID: %d' %os.getpid())


fh = open('test.txt', 'w')


input('Antes de redireccionar')
sys.stderr = fh
print('Esta línea va a test.txt', file=sys.stderr)

sys.Popen('ccc')

input('Despues de redireccionar')


sys.stderr = sys.__stderr__

fh.close()
