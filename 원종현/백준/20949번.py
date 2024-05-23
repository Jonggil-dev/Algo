import math

N = int(input())
li = []

for i in range(N):
    W, H = map(int, input().split())
    li.append((i + 1, math.sqrt(W ** 2 + H ** 2)))

li.sort(key=lambda x: (-x[1], x[0]))

for i in li:
    print(i[0])