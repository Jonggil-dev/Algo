n = int(input())
T = []
P = []
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

result = [0] * (n + 1)

for i in range(n):
    if i + T[i] <= n:
        result[i + T[i]] = max(result[i + T[i]], result[i] + P[i])
    for j in range(i + T[i], n + 1):
        result[j] = max(result[j], result[i + T[i]])

print(max(result))
