import asyncio
import time
import os
import threading


async def say_after(delay, what):
    print(f"T: started at {time.strftime('%X')}")
    print('PID: ', os.getpid(), 'Threading: ', threading.current_thread())
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(main())
