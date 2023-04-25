import sys, os

print("PID: %d" % os.getpid())

print("Coming through stdout")

# stdout is saved
save_stdout = sys.stdout

fh = open("/tmp/test.txt","w")

input("antes de redireccionar")
sys.stdout = fh
print("This line goes to test.txt")
input("despues de redireccionar")
# return to normal:
sys.stdout = save_stdout
print("saliendo...")

fh.close()

