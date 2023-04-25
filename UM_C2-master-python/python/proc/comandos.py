import os

command = " "
while (command != "exit"):
    command = input("Commando: ")
    handle = os.popen(command)
    line = " "
    while line:
        line = handle.read()
        print("--->" + line)
    handle.close()

print("bye!")

