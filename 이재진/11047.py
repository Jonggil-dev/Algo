import sys
N, K = map(int,input().split())
ls = [int(sys.stdin.readline().strip()) for _ in range(N)]
ls.sort(reverse=True)
res = 0
for m in ls:
    if m < K:
        tmp = K // m
        K -= tmp * m
        res += tmp
    elif m == K:
        res += 1
        break
    if K == 0:
        break
print(res)