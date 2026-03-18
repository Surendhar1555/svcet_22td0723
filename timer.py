import time
import sys

h = 0
m = 0
s = 0

while True:
    sys.stdout.write("\r{:02d}:{:02d}:{:02d}".format(h, m, s))
    sys.stdout.flush()
    time.sleep(1)

    s += 1

    if s == 60:
        s = 0
        m += 1

    if m == 60:
        m = 0
        h += 1

    if h == 12:
        h = 0