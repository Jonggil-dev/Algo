from collections import deque
import sys
input=sys.stdin.readline

N,P=map(int,input().split())

graph=[[] for _ in range(N+1)]
capacity=[[0]*(N+1) for _ in range(N+1)]
flow=[[0]*(N+1) for _ in range(N+1)]

for _ in range(P):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    capacity[a][b]=1


def bfs(source,sink,visit):
    q=deque()
    q.append(source)
    while q and visit[sink]==-1:
        a=q.popleft()
        for b in graph[a]:
            if visit[b]==-1 and capacity[a][b]-flow[a][b]>0:
                q.append(b)
                visit[b]=a
                if b==sink:
                    break
    if visit[sink]==-1:
        return 0
    return 1

def karp(source,sink):
    res=0
    while True:
        visit=[-1]*(N+1)
        if not bfs(source,sink,visit):
            break
        b=sink
        while b!=source:
            a=visit[b]
            flow[a][b]+=1
            flow[b][a]-=1
            b=a

        res+=1
    return res
print(karp(1,2))