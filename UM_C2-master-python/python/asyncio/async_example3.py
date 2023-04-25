import asyncio
import time

async def encontrar_divisibles(rango, div_por):
    print("Buscando numeros en el rango {} divisibles por {}".format(rango, div_por))
    encontrado = []
    for i in range(rango):
        if i % div_por == 0:
            encontrado.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)
    print("Listo con nums en el rango {} divisibles por {}".format(rango, div_por))
    return encontrado

async def main():
    divs1 = encontrar_divisibles(5080000, 34113)
    divs2 = encontrar_divisibles(100052, 3210)
    divs3 = encontrar_divisibles(500, 3)
    print("esperando....")
    time.sleep(1)
    resultado = await asyncio.gather(divs1, divs2, divs3)
    #return divs1,divs2,divs3
    return resultado


if __name__ == '__main__':
    resultado = asyncio.run(main())
    print(resultado)
