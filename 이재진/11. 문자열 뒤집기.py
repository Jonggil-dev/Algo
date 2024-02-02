import sys
x = list(map(int, sys.stdin.readline()))
res = [0, 0]
for i in range(2):
    now = 0
    while now <= len(x)-1:
        if x[now] == i:
            now += 1
        else:
            while now <= len(x)-1 and x[now] != i:
                now += 1
            res[i] += 1
print(min(res))