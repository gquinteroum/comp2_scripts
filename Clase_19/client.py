# Cliente
import socket

# Crear un socket IPv6 para cliente
client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Dirección del servidor y puerto
server_address = ('::1', 9999)  # Usamos '::1' como la dirección IPv6 local y el puerto 12345

# Mensaje a enviar
message = "Hola, servidor"

try:
    # Enviar datos
    client_socket.sendto(message.encode(), server_address)

    # Recibir respuesta
    data, server = client_socket.recvfrom(1024)
    print(f"Recibido desde el servidor: {data.decode()}")
finally:
    client_socket.close()
