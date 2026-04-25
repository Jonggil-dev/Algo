from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
li=[[] for _ in range(N+1)]
deg=[0]*(N+1)
time=[0]*(N+1)
for i in range(1,N+1):
    tmp=list(map(int,input().split()))
    t,*l,_=tmp
    time[i]=t
    for j in l:
        li[j].append(i)
        deg[i]+=1
res=[0]*(N+1)
q=deque()
for i in range(1,N+1):
    if deg[i]==0:
        q.append(i)

while q:
    now=q.popleft()
    res[now]+=time[now]
    for i in li[now]:
        deg[i]-=1
        res[i]=max(res[i],res[now])
        if deg[i]==0:
            q.append(i)
print(*res[1:],sep="\n")
