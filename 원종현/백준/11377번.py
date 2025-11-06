from collections import deque
import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
graph=[[] for _ in range(N+M+3)]
capacity=[[0]*(N+M+3) for _ in range(N+M+3)]
flow=[[0]*(N+M+3) for _ in range(N+M+3)]

source=0
sink=0+N+M+1
branch=0+N+M+2
for i in range(1,N+1):
    graph[0].append(i)
    graph[i].append(0)
    capacity[0][i]=1
    graph[branch].append(i)
    graph[i].append(branch)
    capacity[branch][i]=1
graph[0].append(branch)
graph[branch].append(0)
capacity[0][branch]=K
for i in range(N+1,N+M+2):
    graph[i].append(sink)
    graph[sink].append(i)
    capacity[i][sink]=1

for i in range(1,N+1):
    _,*li=list(map(int,input().split()))
    for j in li:
        graph[i].append(N+j)
        graph[N+j].append(i)
        capacity[i][N+j]=1

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
    return 1 if visit[sink]!=-1 else 0

res=0
while True:
    visit=[-1]*(N+M+3)
    if not bfs(source,sink,visit):
        break
    b=sink
    while b!=source:
        a=visit[b]
        flow[a][b]+=1
        flow[b][a]-=1
        b=a
    res+=1
print(res)