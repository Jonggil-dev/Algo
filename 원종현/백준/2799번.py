M,N=map(int,input().split())
res=[0]*5
li=[input() for _ in range(5*M+1)]
tmp=[0]*N
for i in range(1,5*M+1):
    if not i%5:
        for j in range(N):
            res[tmp[j]]+=1
        tmp=[0]*N
        continue
    for j in range(1,5*N+1,5):
        if li[i][j]=="*":
            tmp[j//5]+=1
print(*res)