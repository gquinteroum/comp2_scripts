import os
import sys
import time



#def main():
#    var = 100
#    print("PADRE: Soy el proceso padre y mi pid es: %d" % os.getpid())
#
#    pid = os.fork()
#    
#    for i in range(10):
#      if (pid): # Este es el proceso padre
#          var += 1
#          print("PADRE var: %d  --- %d" % (var, id(var)))
#          time.sleep(1)
#      
#      else: # Proceso hijo
#          var -= 1
#          print("HIJO var: %d  --- %d" % (var, id(var)))
#          time.sleep(1)
#
#if __name__ == "__main__":
#  main()
  


var = 100
print("PADRE: Soy el proceso padre y mi pid es: %d" % os.getpid())

pid = os.fork()

for i in range(10):
  if (pid): # Este es el proceso padre
      var += 1
      print("PADRE var: %d  --- %d" % (var, id(var)))
      time.sleep(1)
  
  else: # Proceso hijo
      var -= 1
      print("HIJO var: %d  --- %d" % (var, id(var)))
      time.sleep(1)


