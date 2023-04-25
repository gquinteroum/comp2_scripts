import asyncio
async def eternity():
    # Sleep for one hour
    print(asyncio.current_task())
    print(asyncio.all_tasks())
    await asyncio.sleep(110)
    print('yay!')

async def main():
    # Wait for at most 1 second
    print(asyncio.current_task())
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())
