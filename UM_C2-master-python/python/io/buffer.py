import time
f = open("/tmp/file","w+", 3)
print(f.line_buffering)
for i in range(5):
        time.sleep(1)
        f.write(str(i))
        #f.flush()

