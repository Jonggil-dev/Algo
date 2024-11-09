N=int(input())
li=[[N]*(N) for i in range(N)]
res=[0]*(N)
for i in range(N):
    li[i][i]=0
while True:
    a,b=map(int,input().split())
    if a+b<0:break
    li[a-1][b-1],li[b-1][a-1]=1,1

for k in range(N):
    for i in range(N):
        for j in range(N):
            li[i][j]=min(li[i][j],li[i][k]+li[k][j])
for i in range(N):
    res[i]=max(li[i])
print(min(res),res.count(min(res)))
print(*[i for i in range(N) if res[i]==min(res)])