import asyncio

# Definir una función asincrónica
async def tarea_espera():
    print("Inicio de la tarea de espera")
    await asyncio.sleep(2)  # Espera durante 2 segundos (simulando una operación lenta)
    print("Fin de la tarea de espera")

# Definir una función asincrónica
async def tarea_impresion():
    print("Inicio de la tarea de impresión")
    await asyncio.sleep(5)
    print("Hola, soy una tarea de impresión")
    print("Fin de la tarea de impresión")

# Definir una función asincrónica
async def tarea_suma():
    print("Inicio de la tarea de suma")
    await asyncio.sleep(3)
    resultado = 10 + 20
    print(f"El resultado de la suma es {resultado}")
    print("Fin de la tarea de suma")

# Crear un bucle de eventos de asyncio
async def main():
    tarea1 = asyncio.create_task(tarea_espera())  # Crear una tarea asincrónica
    tarea2 = asyncio.create_task(tarea_impresion())
    tarea3 = asyncio.create_task(tarea_suma())

    await tarea1  # Esperar a que la tarea de espera termine
    await tarea2  # Esperar a que la tarea de impresión termine
    await tarea3  # Esperar a que la tarea de suma termine

# Ejecutar el bucle de eventos de asyncio
asyncio.run(main())
