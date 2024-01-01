N, M, K = map(int, input().split())
ls = sorted(list(map(int, input().split())), reverse=True)
res = 0
while True:
    for i in range(K):
        if M == 0:
            break
        res += ls[0]
        M -= 1
    if M == 0:
        break
    res += ls[1]
    M -= 1
print(res)