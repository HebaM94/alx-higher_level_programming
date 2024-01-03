#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -1):
    if x % 2 == 0:
        y = 0
    else:
        y = 32
    print('{}'.format(chr(x - y)), end="")
