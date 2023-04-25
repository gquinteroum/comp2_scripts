import asyncio
async def set_after(fut, delay, value):
    print("Empezando %s" % value)
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future.
    fut.set_result(value)
    print("almacenando resultado (espera %d, (%s))" % (delay, value))

async def main():
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut1 = loop.create_future()
    fut2 = loop.create_future()
    fut3 = loop.create_future()

    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # we already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task( set_after(fut1, 2, '... primera') )
    loop.create_task( set_after(fut2, 5, '... segunda') )
    loop.create_task( set_after(fut3, 3, '... tercera') )

    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    print(await fut1)
    print(await fut2)
    print(await fut3)

asyncio.run(main())
