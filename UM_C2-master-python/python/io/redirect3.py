import sys

#save_stderr = sys.stderr
fh = open("/tmp/errors.txt","w")
sys.stderr = fh

print("Esto sale a salida estandar")
print ("printing to error.txt", file=sys.stderr)

# return to normal:
sys.stderr = sys.__stderr__

fh.close()

