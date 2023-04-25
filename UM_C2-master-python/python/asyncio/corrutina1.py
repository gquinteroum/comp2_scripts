import asyncio
import time

async def fecha(nombre):
    while True:
        print (nombre, time.localtime()[3:6] )
        await asyncio.sleep(0.5)


async def a_main():
    try:
        await asyncio.wait_for(fecha("hola"),5)
    except asyncio.TimeoutError:
        print ("se termino el tiempo")

asyncio.run(a_main())
