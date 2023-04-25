import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    # creo dos corutinas asincronicas
    task1 = say_after(4, 'hello')
    task2 = say_after(2, 'world')

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await asyncio.gather(task1,task2)

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
