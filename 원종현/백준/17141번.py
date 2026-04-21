from itertools import combinations
from collections import deque,defaultdict
import sys
input=sys.stdin.readline
d=[0,0,1,-1]
def func(tar):
    cnt=[0,0]
    q=deque()
    visit={}
    for x,y in tar:
        q.append((x,y))
        visit[(x,y)]=0

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 0<=nx<N and 0<=ny<N and li[nx][ny]!=1 and (nx,ny) not in visit:
                cnt[0]=max(cnt[0],visit[(x,y)]+1)
                visit[(nx,ny)]=visit[(x,y)]+1
                q.append((nx,ny))
                cnt[1]+=1
    return 10**9 if cnt[1]!=r else cnt[0]
N,M=map(int,input().split())
li=[]
tar=[]
r=0
for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(N):
        if tmp[j]==2:
            tar.append((i,j))
            r+=1
        if tmp[j]==0:
            r+=1
    li.append(tmp)

r-=M
res=10**9
for i in combinations(tar,M):
    res=min(res,func(i))
print(res if res!=10**9 else -1)