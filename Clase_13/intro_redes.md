<p align="center">
  <img src="images/um_logo.png">
</p>

#Una muy micro introducción a las redes de computadoras
Este documento tiene como propósito ofrecer una breve introducción al fascinante mundo de las redes de computadoras. Es importante señalar que el contenido aquí presentado no busca proporcionar un estudio exhaustivo o detallado sobre el tema de las redes, sino que está diseñado específicamente como un preludio para comprender mejor el concepto de sockets y su aplicación en la programación.

En este material introductorio, se presentarán conceptos fundamentales relacionados con las redes de computadoras, tales como la estructura básica de una red, el funcionamiento de los dispositivos de red, la comunicación entre computadoras y la transmisión de datos a través de los protocolos de red.

Es fundamental destacar que el ámbito de las redes de computadoras es amplio y complejo, y abarca una gran cantidad de tecnologías y protocolos. El objetivo de esta introducción es proporcionar a los estudiantes una visión general y una base para comprender mejor los conceptos más específicos que se abordarán en el tema de los sockets.

Se alienta a los lectores interesados en profundizar en el mundo de las redes de computadoras a buscar fuentes adicionales y material especializado para adquirir un conocimiento más completo.

## Las redes de computadoras
Las redes de computadoras son fundamentales en nuestro mundo digital actual, permitiendo conectar y comunicar dispositivos y servicios a nivel global, facilitando el intercambio eficiente de información y recursos.

Una red de computadoras es un conjunto interconectado de dispositivos informáticos, como computadoras, servidores, dispositivos móviles y otros equipos, que pueden comunicarse y compartir recursos.

El funcionamiento de una red se basa en la transferencia de datos a través de cables, conexiones inalámbricas o señales de luz, enviados en pequeños paquetes y reensamblados en su destino.

Estas redes pueden variar en alcance y topología. Por ejemplo, las redes LAN (Local Area Network) se utilizan generalmente en espacios limitados, como oficinas o casas, mientras que las redes WAN (Wide Area Network) abarcan áreas más grandes, como ciudades o países enteros.

Las redes pueden tener diferentes topologías, como estrella, bus o anillo, definiendo la forma en que los dispositivos se conectan.

Son esenciales para el acceso a internet, la transmisión de datos, el correo electrónico, el comercio electrónico y muchas otras aplicaciones que forman parte de nuestra vida cotidiana.

Las redes de computadoras son la columna vertebral de la comunicación moderna, impulsando la conectividad y la colaboración a nivel global en nuestra sociedad digital. Con el avance de la tecnología, estas redes continúan evolucionando y desempeñando un papel crucial en nuestra vida cotidiana.

## Una ultra breve historia
La historia de las redes de computadoras se remonta a los años 1960, cuando la Agencia de Proyectos de Investigación Avanzados (ARPA) del Departamento de Defensa de Estados Unidos creó la primera red, conocida como ARPANET. Esta red experimental permitió a los investigadores compartir datos y recursos, sentando las bases de lo que eventualmente se convertiría en Internet.

En los años 1970, ARPANET se expandió y se desarrollaron nuevos protocolos de comunicación, como el Protocolo de Control de Transmisión (TCP), que permitieron la interconexión de diferentes redes, dando lugar a la creación de la primera "red de redes", que más tarde se conocería como Internet.

En la década de 1980, se crearon las redes de área local (LAN) para interconectar computadoras en espacios limitados, como oficinas o edificios. Además, surgieron protocolos de comunicación como el Ethernet, que facilitaron la transferencia de datos a alta velocidad en estas redes locales.

En la década de 1990, con la popularización de Internet, se produjo una explosión en la cantidad de usuarios y sitios web, lo que llevó a la creación del World Wide Web (WWW) por Tim Berners-Lee. Esto permitió un acceso fácil y rápido a la información a través de navegadores web, lo que impulsó aún más la adopción masiva de Internet en todo el mundo.

Con el avance de la tecnología en el siglo XXI, las redes de computadoras se han vuelto más rápidas, seguras y versátiles. El desarrollo de redes inalámbricas y móviles ha permitido la conectividad en cualquier lugar y en cualquier momento, llevando la comunicación y el acceso a la información a niveles nunca antes imaginados.

## Desafíos y problemas en la creación de redes de computadoras
La creación de redes de computadoras es un proceso complejo que implica enfrentar diversos desafíos y problemas para lograr un funcionamiento eficiente y confiable. Desde los primeros días de las redes de computadoras, los ingenieros y expertos se encontraron con dificultades para diseñar sistemas que pudieran comunicarse de manera efectiva y segura.

Uno de los principales problemas radica en la complejidad inherente de las redes de computadoras. Estos sistemas deben lidiar con una amplia gama de dispositivos, protocolos, topologías y requisitos de rendimiento. Además, conforme la cantidad de dispositivos y servicios conectados aumenta, la administración y el mantenimiento de la red se vuelven cada vez más desafiantes.

Otro desafío crucial es la compatibilidad entre dispositivos y sistemas de diferentes fabricantes. A medida que la tecnología de redes avanza rápidamente, la interoperabilidad entre equipos se vuelve esencial para asegurar una comunicación sin problemas. Sin embargo, lograr la compatibilidad entre diferentes plataformas puede ser complicado debido a las variaciones en la implementación de estándares y protocolos.

La seguridad es otra preocupación crucial en la creación de redes de computadoras. Las redes están constantemente expuestas a amenazas externas e internas, como piratas informáticos, malware y ataques cibernéticos. Por lo tanto, es imperativo implementar medidas de seguridad robustas para proteger los datos y garantizar la confidencialidad, integridad y disponibilidad de la red.

Además, la creciente cantidad de servicios y aplicaciones que utilizan las redes de computadoras ha llevado a un aumento en la demanda de ancho de banda y rendimiento. Los ingenieros deben abordar el desafío de optimizar el rendimiento de la red y reducir la latencia para satisfacer las necesidades de los usuarios y garantizar una experiencia fluida.

Ante estos desafíos y problemas, surgió la necesidad de un enfoque estructurado y organizado para el diseño y la implementación de redes de computadoras.

## El modelo de capas OSI
El modelo OSI (Open Systems Interconnection) es un marco de referencia conceptual que define una arquitectura de red en capas. Fue desarrollado por la Organización Internacional de Normalización (ISO) en la década de 1980 y se utiliza como una guía para diseñar y comprender cómo funcionan las redes de computadoras.

El modelo OSI consta de siete capas, cada una con funciones específicas y bien definidas. Estas capas son:


|CAPA| NOMBRE  | DESCRIPCIÓN |
|---|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 7 | APLICACIÓN      | Es la capa más alta del modelo y proporciona interfaces para que las  aplicaciones de usuario accedan a los servicios de red, como el correo  electrónico, navegación web, transferencia de archivos, etc.                                                                                                   |
| 6 | PRESENTACIÓN    | Se encarga de la representación y el formato de los datos, asegurando  que los dispositivos puedan interpretar la información correctamente.                                                                                                                                                                 |
| 5 | SESIÓN          | Establece, mantiene y finaliza sesiones entre aplicaciones en  dispositivos diferentes. También permite la sincronización y el control  de diálogo entre las aplicaciones.                                                                                                                                   |
| 4 | TRANSPORTE      | Ofrece servicios de transporte de extremo a extremo multiplexando la información para que varios procesos puedan comunicarse desde un mismo host. Puede crear mecanismos para que los datos se entreguen de manera confiable y ordenada. Esta capa también  maneja la fragmentación y reensamblaje de datos. |
| 3 | RED             | Es responsable de enrutar los paquetes de datos a través de la red desde el origen hasta el destino.                                                                                                                                                                                                         |
| 2 | ENLACE DE DATOS | Gestiona la comunicación entre dispositivos directamente conectados en  una red local. Se encarga de la detección y corrección de errores, así  como de controlar el flujo de datos.                                                                                                                         |
| 1 | FÍSICA          | Se encarga de la transmisión y recepción de señales eléctricas, ópticas o  inalámbricas a través del medio de transmisión físico, como cables o  ondas de radio.                                                                                                                                             |


## El modelo TCP/IP
Aunque el modelo OSI es una guía conceptual valiosa, no se utiliza ampliamente como marco de referencia en la implementación real de redes de computadoras. Existen varias razones para esto:

- Complejidad: El modelo OSI consta de siete capas, cada una con funciones específicas y bien definidas. Esto puede hacer que sea complicado de implementar en la práctica, especialmente en redes más pequeñas o menos complejas.

- Redundancia: Algunas de las capas del modelo OSI realizan funciones similares a las de otras capas. Esto puede dar lugar a una cierta redundancia y complejidad innecesaria en la implementación.

- Modelo TCP/IP: A medida que Internet se convirtió en la red dominante a nivel mundial, el modelo TCP/IP ganó popularidad. El modelo TCP/IP, que consta de cuatro capas (capa de acceso al medio, capa de internet, capa de transporte y capa de aplicación), se ajustaba más estrechamente a la arquitectura y funcionalidad de Internet, lo que lo hizo más práctico y eficiente para su uso en el mundo real.

El modelo TCP/IP fue desarrollado por encargo del Departamento de Defensa de los Estados Unidos y se convirtió en el protocolo estándar para las comunicaciones en Internet. A diferencia del modelo OSI, que es más abstracto, el modelo TCP/IP se basa en protocolos y está más orientado a la implementación real de redes.

El modelo TCP/IP sigue siendo el modelo que se utiliza en la actualidad, no solo para Internet, sino también para redes privadas y corporativas. Su simplicidad, eficiencia y capacidad para adaptarse a diferentes entornos han contribuido a su popularidad y uso generalizado en la industria de las redes de computadoras.

| CAPA | NOMBRE     | DESCRIPCIÓN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | EJEMPLOS DE PROTOCOLOS     |
|------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| 7    | APLICACIÓN | Se ocupa de las interacciones directas con las aplicaciones del usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | HTTP; SMTP; FTP; DNS; etc  |
| 4    | TRANSPORTE | La capa de transporte en el modelo TCP/IP se encuentra justo encima de  la capa de Internet y tiene la función de permitir una comunicación de  extremo a extremo entre entidades pares en los nodos de origen y  destino. Al igual que en la capa de transporte del modelo OSI, aquí se  definen dos protocolos clave: TCP (Protocolo de Control de la  Transmisión) y UDP (Protocolo de Datagrama de Usuario).                                                                                                                          | TCP; UDP                   |
| 3    | INTERNET   | Es una de las capas clave en el modelo TCP/IP y desempeña un papel  central al mantener la cohesión en toda la arquitectura de la red. La  función principal de esta capa es permitir que los hosts envíen paquetes  a cualquier red y que viajen de manera independiente hacia su destino,  incluso si se encuentran en redes diferentes. Los paquetes pueden llegar  en un orden distinto al que se enviaron originalmente, por lo que es  responsabilidad de las capas superiores reorganizarlos si se requiere  una entrega en orden. | IP; ICMP                   |
| 2    | ENLACE     | Se encarga de establecer enlaces entre los dispositivos y los distintos  medios de transmisión, como líneas seriales y Ethernet clásica. Su  función principal es proporcionar una red de conmutación de paquetes sin  conexión, que permite la transferencia eficiente de datos a través de  diversas redes. Aunque técnicamente no es una capa en el sentido común,  actúa como una interfaz esencial para garantizar una interconexión  coherente y efectiva en el modelo.                                                             | ETHERNET; 802.11; DSL; etc |


## Relación entre los modelos OSI y TCP/IP
A continuación se muestra una relación aproximada entre los dos modelos.

|   | OSI             | TCP/IP     |
|---|-----------------|------------|
| 7 | Aplicación      | Aplicación |
| 6 | Presentación    |            |
| 5 | Sesión          |            |
| 4 | Transporte      | Transporte |
| 3 | Red             | Internet   |
| 2 | Enlace de datos | Enlace     |
| 1 | Física          |            |

## Los puertos
Los puertos, son una parte esencial del modelo TCP/IP que opera en la capa de transporte. En la arquitectura de red, los puertos proporcionan una forma de direccionar el tráfico de datos hacia los diferentes servicios o aplicaciones que se ejecutan en un dispositivo dentro de una red.

Los puertos son una especie de dirección lógica que identifica los diferentes procesos en un mismo host.

Los números de puerto por debajo del valor 1024 están reservados para servicios estándar que generalmente solo pueden ser iniciados por usuarios con privilegios, como el usuario "root" en sistemas UNIX. Estos puertos se conocen como "puertos bien conocidos".

La lista completa de puertos bien conocidos está disponible en el sitio web [www.iana.org](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml) y contiene más de 700 asignaciones. Estos puertos permiten que los servicios y aplicaciones comunes funcionen de manera consistente y se comuniquen correctamente en una red, lo que es esencial para el correcto funcionamiento de la infraestructura de Internet. Los usuarios privilegiados, como administradores de sistemas, pueden configurar y gestionar estos puertos para asegurar una comunicación eficiente y segura dentro de la red.