import asyncio
import os
import random

async def count():
    t = random.randint(1,10)
    print(asyncio.current_task())
    print("Esperando: %d segundos" % t)
    print("One %d" % os.getpid())
    await asyncio.sleep(t)
    print("Two %d" % os.getpid())

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
