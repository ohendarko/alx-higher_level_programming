#!/usr/bin/python3
m = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - m)), end="")
    m = 32 if m == 0 else 0
