import asyncio

# Definir una función asincrónica
async def hola_mundo():
    print("Esperando...")
    await asyncio.sleep(1)  # Espera durante 1 segundo (simulando una operación lenta)
    print("¡Hola, mundo!")

# Crear un bucle de eventos de asyncio
async def main():
    await hola_mundo()  # Ejecutar la función asincrónica

# Ejecutar el bucle de eventos de asyncio
asyncio.run(main())


