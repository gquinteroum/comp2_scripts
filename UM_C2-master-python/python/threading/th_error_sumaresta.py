import threading

num = 5

def sumador(value):
    global num
    for i in range(value):
        num = num+1


def restador(value):
    global num
    for i in range(value):
        num = num - 1


if __name__ == "__main__":
    th1 = threading.Thread(target=sumador, args=(1000000,))
    th2 = threading.Thread(target=restador, args=(1000000,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print("Saldo: ", num)

