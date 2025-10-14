from collections import deque
import sys
input=sys.stdin.readline

def conv(x):
    if x.isupper():
        return ord(x)-ord('A')
    else:
        return ord(x)-ord('a')+26

def bfs(st,end,visit):
    q=deque()
    q.append(st)
    while q:
        now=q.popleft()
        for next in graph[now]:
            if capa[now][next]-flow[now][next]>0 and visit[next]==-1:
                q.append(next)
                visit[next]=now
                if next==end:
                    return 1
    return 0

def func(st,end):
    tmp=0
    while True:
        visit=[-1]*(52)
        if not bfs(st,end,visit):
            break
        min_v=10**9
        cur=end
        while cur!=st:
            min_v=min(min_v,capa[visit[cur]][cur]-flow[visit[cur]][cur])
            cur=visit[cur]
        cur=end
        while cur!=st:
            flow[visit[cur]][cur]+=min_v
            flow[cur][visit[cur]]-=min_v
            cur=visit[cur]
        tmp+=min_v
    return tmp

N=int(input())
capa=[[0]*(52) for _ in range(52)]
flow=[[0]*(52) for _ in range(52)]
graph=[[] for _ in range(52)]
for _ in range(N):
    a,b,c=input().rstrip().split()
    a=conv(a)
    b=conv(b)
    c=int(c)
    capa[a][b]+=c
    capa[b][a]+=c
    graph[a].append(b)
    graph[b].append(a)

res=func(conv('A'),conv('Z'))
print(res)