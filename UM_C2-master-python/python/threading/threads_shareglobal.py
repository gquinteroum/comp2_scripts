import threading

num = 10
def f1(n):
    global num
    num=100

def f2(n):
    global num
    num=200

if __name__ == "__main__":
    t1 = threading.Thread(f1, args=(1,))
    t2 = threading.Thread(f2, args=(2,))

    t1.start()
    t2.start()
    print("Numero: ", num)
