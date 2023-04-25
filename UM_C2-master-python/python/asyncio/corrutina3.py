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
    t1 = asyncio.create_task(fecha("c1"))
    t2 = asyncio.create_task(fecha("c2"))
    t3 = asyncio.create_task(fecha("otra"))
    await t1
    await t2
    await t3


asyncio.run(a_main())
