import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
tree=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
visit=[0]*(N+1)
def get(x):
    visit=[0]*(N+1)
    visit[x]=1
    res=[0,-1]
    q=deque()
    q.append((x,0))
    while q:
        now,dist=q.popleft()
        for i in tree[now]:
            cost=dist+1
            if not visit[i]:
                q.append((i,cost))
                visit[i]=1
                if cost>res[1]:
                    res=[i,cost]
    return res
A,B=get(1)
print((get(A)[1]+1)//2)