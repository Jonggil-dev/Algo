import sys

N = int(input())
res = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        res.append(num)
    else:
        res.pop()
print(sum(res))