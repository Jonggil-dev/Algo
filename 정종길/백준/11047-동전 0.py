N, K = map(int,input().split())
coins = []
res = 0

for _ in range(N):
    coins.append(int(input()))

for coin in coins[::-1]:
    while K > 0:
        K -= coin
        res += 1
    if K == 0:
        break
    K += coin
    res -= 1

print(res)