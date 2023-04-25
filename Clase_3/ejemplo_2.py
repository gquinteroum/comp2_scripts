"""
Se puede ver como os.system es una función bloqueante. Por lo tanto debe esperar a que termine el primer proceso para comenzar el siguiente
"""

import os

for i in range(2):
  os.system("python ejemplo_1.py")
