N,M=map(int,input().split())
check=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    check[a][b]=1
    check[b][a]=1

res=0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        for k in range(j+1,N+1):
            if not check[i][j] and not check[i][k] and not check[k][j]:
                res+=1

print(res)

