N,M=map(int,input().split())
li=[input() for _ in range(N)]
ch=[[0]*(M) for _ in range(N)]
res=0
for i in range(N):
    for j in range(M):
        if li[i][j]=='-' and not ch[i][j]:
            res+=1
            tmp=j+1
            while True:
                if tmp<M and li[i][tmp]=='-' and not ch[i][tmp]:
                    ch[i][tmp]=1
                    tmp+=1
                else:
                    break
        elif li[i][j]=='|' and not ch[i][j]:
            tmp=i+1
            res+=1
            while True:
                if tmp<N and li[tmp][j]=='|' and not ch[tmp][j]:
                    ch[tmp][j]=1
                    tmp+=1
                else:
                    break
print(res)