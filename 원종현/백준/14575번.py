N, T = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

st, end = 1,10**9
res =10**9
while st <= end:
    mid = (st + end) // 2
    a, b = 0, 0
    for i in range(N):
        if li[i][0] > mid:
            a = -1
            break
        a += li[i][0]
        b += min(mid, li[i][1])
    if a == -1 or b < T:
        st = mid + 1
    else:
        if a <= T <= b:
            res = min(res, mid)
        end = mid - 1

print(res if res != 10**9 else -1)
