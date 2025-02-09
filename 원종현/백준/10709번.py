H,W=map(int,input().split())
li=[input() for _ in range(H)]
res=[[0]*(W) for _ in range(H)]

for i in range(H):
    res=[-1]*W
    for j in range(W):
        if li[i][j]=='c':
            res[j]=0
    tmp=0
    for j in range(1,W):
        if res[j]==0:
            tmp=0
        if res[j-1]!=-1 and res[j]!=0:
            tmp+=1
            res[j]=tmp
    print(*res)