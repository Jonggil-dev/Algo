N = int(input())
q = list(range(1,N+1))
for _ in range(N-1):
    print(q.pop(0))
    q.append(q.pop(0))
print(*q)