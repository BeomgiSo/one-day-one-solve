# 프린트 큐
# 1966번

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = list(map(int, sys.stdin.readline().split()))
    imp = list(map(int, sys.stdin.readline().split()))
    order = 0

    while 1:
        if imp[0] == max(imp):
            order += 1
            if y == 0:
                print(order)
                break
            else:
                y -= 1
                imp.pop(0)
        else:
            imp.append(imp[0])
            imp.pop(0)
            if y == 0:
                y = len(imp)-1
            else:
                y -= 1
