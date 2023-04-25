import sys

while True:
  # output to stdout:
  print("iterando ...")
  try:
      number = input("Ingrese un numero: ")
  except EOFError:
      print("\nBye")
      break
  else:
      try:
         number = int(number)
      except ValueError:
         print("\nNumero invalido", file=sys.stderr)
         continue
      if number == 0:
         print("0 no tiene inverso", file=sys.stderr)
      else:
         print("El inverso de %d es %f" % (number, 1.0/number) )
