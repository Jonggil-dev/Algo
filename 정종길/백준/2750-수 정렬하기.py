N = int(input())
res = []
for _ in range(N):
    res.append(int(input()))

res.sort()
for num in res:
    print(num)