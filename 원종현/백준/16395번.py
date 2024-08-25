N,K=map(int,input().split())
li=[[] for _ in range(N)]

for i in range(N):
    for j in range(i+1):
        if i==0 or j==0 or j==i:
            li[i].append(1)
        else:
            li[i].append(li[i-1][j-1]+li[i-1][j])
print(li[N-1][K-1])