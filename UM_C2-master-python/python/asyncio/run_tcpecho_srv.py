import asyncio
import time

async def handle_echo(reader, writer):
    #print(f"Esperando datos del cliente (durmiendo {asyncio.all_tasks()})")
    for t in asyncio.all_tasks():
        print(f"Tarea: {t}")
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    print("encolando el mayuscula")
    writer.write(data.upper())
    print("ejecutando el drain()")
    await writer.drain()

    print("Close the connection")
    writer.close()
    for t in asyncio.all_tasks():
        print(f"Cerrando Tarea: {t}")

async def main():
    server = await asyncio.start_server(
        handle_echo, '0.0.0.0', 1234)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr} {asyncio.current_task()}')

#    async with server:
    print(f"Tareas:\n{asyncio.all_tasks()}")
    await server.serve_forever()

asyncio.run(main())
