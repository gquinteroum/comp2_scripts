
import asyncio
import time

async def fecha(nombre):
    while True:
        print (nombre, time.localtime()[3:6] )
        await asyncio.sleep(0.5)

#async def a_main():
#    await (fecha("c1"))
#    await (fecha("c2"))
#    await (fecha("otra"))
#asyncio.run(a_main())

async def a_main():
    await asyncio.gather ( fecha("c1"), fecha("c2"), fecha("otra"))
asyncio.run(a_main())
