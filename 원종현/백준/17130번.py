from collections import deque
import sys
input=sys.stdin.readline
d=[(1,1),(0,1),(-1,1)]

N,M=map(int,input().split())
li=[]
st=[]
hole=[]
for i in range(N):
    tmp=input().rstrip()
    for j in range(M):
        if tmp[j]=='R':
            st=[i,j]
        elif tmp[j]=='O':
            hole.append((i,j))
    li.append(tmp)

visit=[[0]*M for _ in range(N)]
visit[st[0]][st[1]]=1

dp=[[0]*M for _ in range(N)]
dp[st[0]][st[1]]=1
while 0<=st[0]<N and 0<=st[1]<M:
    x,y=st[0],st[1]
    while 0<=x<N and 0<=y<M:
        tmp=[0,0,0]
        if li[x][y]!='#':
            if 0<=x-1<N and 0<=y-1<M and visit[x-1][y-1]:
                tmp[0]=dp[x-1][y-1]+(1 if li[x-1][y-1]=='C' else 0)
                visit[x][y]=1
            if 0<=x<N and 0<=y-1<M and visit[x][y-1]:
                tmp[1]=dp[x][y-1]+(1 if li[x][y-1]=='C' else 0)
                visit[x][y]=1
            if 0<=x+1<N and 0<=y-1<M and visit[x+1][y-1]:
                tmp[2]=dp[x+1][y-1]+(1 if li[x+1][y-1]=='C' else 0)
                visit[x][y]=1
        dp[x][y]=max(dp[x][y],max(tmp))
        x-=1
        y+=1
    if 0<=st[0]+1<N:
        st[0]+=1
    else:
        st[1]+=1

res=0
for x,y in hole:
    res=max(res,dp[x][y])
print(res-1)