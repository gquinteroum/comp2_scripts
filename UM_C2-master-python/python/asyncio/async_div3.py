import asyncio, os

async def encontrar_divisibles(rango, div_por):
    print("Buscando numeros en el rango {} divisibles por {}".format(rango, div_por))
    located = []
    for i in range(rango):
        if i % div_por == 0:
            located.append(i)
        if i % 50000 == 0:
            print("atando cordones... pid %d" % os.getpid())
            await asyncio.sleep(0.0001)

    print("Listo con nums en el rango {} divisibles por {} ".format(rango, div_por ))
    return located


async def main():
    await asyncio.gather(
            encontrar_divisibles(5080000, 34113),
            encontrar_divisibles(1000520, 3210),
            encontrar_divisibles(500, 3)
            )
    return divs1, divs2, divs3


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        # logging...etc
        pass
