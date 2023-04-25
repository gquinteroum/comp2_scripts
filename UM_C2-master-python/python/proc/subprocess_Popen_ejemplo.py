import subprocess, sys

comando = sys.argv[1]

proceso = subprocess.Popen([comando], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

out,err = proceso.communicate()

print("Salida: \n", out)
print("\nErrores: \n", err)

