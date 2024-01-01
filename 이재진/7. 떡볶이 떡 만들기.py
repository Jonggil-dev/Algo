import sys
N, M = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))
ls.sort()
start, end = ls[0], ls[-1]
res = 0
while start <= end:
    mid = (start+end)//2
    tmp = 0
    for i in ls:
        if i > mid:
            tmp += i-mid
    if tmp < M:
        end = mid-1
    elif tmp > M:
        start = mid+1
        res = mid
    elif tmp == M:
        res = mid
        break
print(res)