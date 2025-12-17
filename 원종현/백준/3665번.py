from collections import deque
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    T=list(map(int,input().split()))
    graph=[set() for _ in range(N+1)]
    ind=[0]*(N+1)
    for i in range(N-1,0,-1):
        for j in range(i-1,-1,-1):
            graph[T[i]].add(T[j])
            ind[T[j]]+=1
    m=int(input())
    for i in range(m):
        a,b=map(int,input().split())
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].add(b)
            ind[b]+=1
            ind[a]-=1
        else:
            graph[a].remove(b)
            graph[b].add(a)
            ind[a]+=1
            ind[b]-=1
    res=[]
    q=deque()
    check=1
    for i in range(1,N+1):
        if ind[i]==0:
            q.append(i)
    while q:
        if len(q)>1:
            check=0
        now=q.popleft()
        res.append(now)
        for i in graph[now]:
            ind[i]-=1
            if ind[i]==0:
                q.append(i)

    if len(res)==N:
        print(*res[::-1])
    elif not check:
        print('?')
    else:
        print('IMPOSSIBLE')