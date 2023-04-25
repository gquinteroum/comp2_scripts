import socket
import threading


def servicio(direccion):
    addrfamily, sockettype, transport, cadena, address = direccion
    s = socket.socket(addrfamily, sockettype)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(address)
    s.listen(1)
    while True:
        s_cli, addr = s.accept()
        print("Socket aceptando conexion en: ", addrfamily)
        print(addr)
        recibido = s_cli.recv(1024)
        respuesta = recibido.decode().upper()
        s_cli.send(respuesta.encode())
        print(respuesta)
        s_cli.close()


if __name__ == "__main__":
    
    direcciones = socket.getaddrinfo("localhost", 1234, socket.AF_UNSPEC, socket.SOCK_STREAM)

    hilos = []
    for direccion in direcciones:
        hilos.append(threading.Thread(target=servicio, args=(direccion,)))

    for h in hilos:
        h.start()
    for h in hilos:
        h.join()
