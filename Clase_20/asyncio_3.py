import asyncio
import aiohttp

async def obtener_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as respuesta:
            contenido = await respuesta.text()
            print(f"URL: {url}, Longitud del contenido: {len(contenido)}")

async def main():
    urls = [
        "https://www.ejemplo.com",
        "https://www.python.org",
        "https://www.google.com"
    ]

    # Crear tareas asincrónicas para obtener las URL de manera concurrente
    tareas = [obtener_url(url) for url in urls]

    # Esperar a que se completen todas las tareas
    await asyncio.gather(*tareas)

# Ejecutar el bucle de eventos de asyncio
asyncio.run(main())

