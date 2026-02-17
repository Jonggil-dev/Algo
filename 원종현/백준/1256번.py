N,M,K=map(int,input().split())
li=[[1]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        li[i][j]=li[i-1][j]+li[i][j-1]

if li[N][M]<K:
    print(-1)
    exit()
res=''
while True:
    if N==0 or M==0:
        res+='z'*M+'a'*N
        break
    now=li[N-1][M]
    if K<=now:
        res+='a'
        N-=1
    else:
        res+='z'
        M-=1
        K-=now
print(res)