import sys
import math
N, M, B = map(int,input().split())
ls = []
for _ in range(N):
    ls.extend(list(map(int, sys.stdin.readline().split())))
height_max, height_min = 0, 256
for i in range(N*M):
    if height_max < ls[i]:
        height_max = ls[i]
    if height_min > ls[i]:
        height_min = ls[i]
tmp = []
min_t = float('inf')
max_h = -1
for h in range(height_min, height_max + 1):
    t = 0
    num = B
    for i in range(N*M):
        if ls[i] > h:
            num += ls[i] - h
            t += 2 * (ls[i] - h)
        elif ls[i] < h:
            num -= h - ls[i]
            t += h - ls[i]
    if num < 0:
        continue
    else:
        if min_t > t:
            min_t = t
            max_h = h
        if min_t == t:
            if max_h < h:
                max_h = h
print(min_t, max_h)