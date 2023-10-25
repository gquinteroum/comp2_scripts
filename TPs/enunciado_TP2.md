# COMPUTACION II


## TP2

Fecha de entrega: 14/11/2023


### Problema

#### A
Es necesario procesar imágenes con python, utilizando bibliotecas de procesamiento de imágenes.
Las imágenes deen enviarse a un servidor HTTP concurrente para poder procesarlas y devolverlas al cliente.
El servidor debe crear un hijo que implemente un servicio no concurrente que convierta las imágenes enviadas del cliente a imágenes en escala de grises.
Es necesario implementar un mecanismo de ipc para que el servidor HTTP solicite trabajo de procesado de imagenes.
El servidor HTTP deberá bloquearse a la espera de la finalización de la conversión de la imagen enviada, necesitando algun mecanismo de sincronización.
El servidor HTTP debe enviar la imagen procesada al cliente y terminar la conexión.

#### B
El servidor debe comunicarse con otro servidor en el mismo host. Este segundo servidor debe reducir el tamaño de la imagen un factor de escala dado por el primer servidor

#### C
Los servicios del servidor de escalado debe ser accesible desde el cliente vía el primer servidor.


### Requerimientos

* La aplicación debe contener como mínimo 3 funciones.
* El servidor HTTP debe poder atender requerimientos ipv4 e ipv6 indistintamente.
* Debe procesar opciones con getopt (agregar una opcion de ayuda) o con argparse. 
* Debe manejar los errores.


#### Ejemplo modo de uso

~~~~~~~~~~~~~~~~~~~
$ ./tp2.py -h
usage: tp2..py [-h] -i IP -p PORT

Tp2 - procesa imagenes

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP Direccion de escucha
  -p PORT, --port PORT  Puerto de escucha



### Objetivos

* Manejo de archivos (apertura, escritura y cierre).
* Creación de hilos/procesos.
* Uso de mecanismos de Inter Process Comunication
* Uso de mecanismos de Sincronización.
* Uso de mecanismos de Socket.

### Referencias
File Upload in HTML
https://www.rfc-editor.org/rfc/rfc1867

### Bonus Track
El servidor debe poder atender requerimientos HTTPS

