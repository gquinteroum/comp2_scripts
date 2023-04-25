
import mmap, sys
import timeit

filename = sys.argv[1]
def regular_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        text = file_obj.read()
        # print(text)

def mmap_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read()
            # print(text)

ret_regular = timeit.repeat(
        "regular_io(filename)",
        repeat=3,
        number=1,
        setup="from __main__ import regular_io, filename")

ret_mmap = timeit.repeat(
        "mmap_io(filename)",
        repeat=3,
        number=1,
        setup="from __main__ import mmap_io, filename")

print("\n\n")
print(ret_regular)
print(ret_mmap)
