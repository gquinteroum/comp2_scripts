import os, time, subprocess

def hijo():
    print("soy el hijo")
    time.sleep(1)
    os._exit(0)


def main():
	ret=os.fork()

	if ret==0:
		hijo()

	print("soy el padre")

	print(subprocess.check_output(["ps", "fax"], universal_newlines=True))
	time.sleep(2)
	print("_________________________________________________________________")
	print(subprocess.check_output(["ps", "fax"], universal_newlines=True))
	os.wait()
	print("=================================================================")
	print(subprocess.check_output(["ps", "fax"], universal_newlines=True))


if __name__ == "__main__":
	main()
	
