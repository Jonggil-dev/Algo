from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
tree=[[] for i in range(N+1)]

for i in range(N-1):
    a,b,c=map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

def func(st):
    q=deque()
    q.append((st,0))
    visit=[0]*(N+1)
    visit[st]=1
    res=[st,0]
    while q:
        now,val=q.popleft()
        if res[1]<val:
            res=[now,val]
        for i,cost in tree[now]:
            if not visit[i]:
                q.append((i,cost+val))
                visit[i]=1
    return res

def func2(st,ex):
    q=deque()
    q.append((st,0))
    visit=[0]*(N+1)
    visit[st]=1
    visit[ex]=1
    res=[st,0]
    while q:
        now,val=q.popleft()
        if res[1]<val and now!=ex:
            res=[now,val]
        for i,cost in tree[now]:
            if not visit[i]:
                q.append((i,cost+val))
                visit[i]=1
    return res

a,v=func(1)
b,v=func(a)
b1,v1=func2(a,b)
a1,v2=func2(b,a)
print(max(v1,v2))