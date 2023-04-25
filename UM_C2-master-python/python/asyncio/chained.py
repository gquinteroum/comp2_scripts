import asyncio
import random
import time

async def primera(n: int) -> str:
    i = random.randint(0, 10)
    print(f"primera({n}) esperando {i}s.")
    await asyncio.sleep(i)
    result = f"result{n}-A"
    print(f"Retornando primera({n}) == {result}.")
    return result

async def segunda(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"segunda{n, arg} esperando {i}s.")
    await asyncio.sleep(i)
    result = f"result{n}-B => {arg}"
    print(f"Retornando segunda{n, arg} => {result}.")
    return result

async def chain(n: int) -> None:
    start = time.perf_counter()
    print("Lanzando primera")
    prim = await primera(n)
    print("Lanzando Segunda")
    segu = await segunda(n, prim)
    end = time.perf_counter() - start
    print(f"-->Encadenado result{n} => {segu} (tomó {end:0.2f} s).")

async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))
    # asyncio.gather( chain(n1), chain(2))
    # default: asyncio.gather( chain(1), chain(2), chain(3))

if __name__ == "__main__":
    import sys
    random.seed(143)
    args = [1, 2, 3] if len(sys.argv) == 1 else list(map(int, sys.argv[1:]))
    print(args)
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
