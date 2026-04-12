from collections import deque
import sys
input=sys.stdin.readline
d=[0,0,1,-1]

def func(st,end):
    visit={}
    visit[(st[0],st[1])]=0
    q=deque()
    q.append((st[0],st[1],0))

    while q:
        x,y,c=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 0<=nx<H and 0<=ny<W and li[nx][ny]!='x' and ((nx,ny) not in visit or visit[(nx,ny)]>c+1):
                if (nx,ny)==end:
                    return c+1
                visit[(nx,ny)]=c+1
                q.append((nx,ny,c+1))
    return -1

def dfs(now,visit):
    if visit==(1<<N)-1:
        return 0
    if (now,visit) in dp:
        return dp[(now,visit)]
    res=10**9
    for next in range(1,N):
        if not (visit&(1<<next)) and dist[now][next]!=-1:
            res=min(res,dfs(next,visit|(1<<next))+dist[now][next])
    dp[(now,visit)]=res
    return res

while True:
    W,H=map(int,input().split())
    if W==0 and H==0:
        break
    li=[]
    st=[]
    tar=[]
    for i in range(H):
        tmp=input().rstrip()
        for j in range(W):
            if tmp[j]=='o':
                st=(i,j)
            elif tmp[j]=='*':
                tar.append((i,j))
        li.append(tmp)
    tar=[st]+tar
    N=len(tar)
    dist=[[-1]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            v=func(tar[i],tar[j])
            dist[i][j]=v
            dist[j][i]=v
    dp={}
    res=dfs(0,1)
    print(res if res!=10**9 else -1)

