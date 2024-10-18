from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
graph=[[]for _ in range(N+1)]
reverse_graph=[[]for _ in range(N+1)]
visit=[0]*(N+1)
val=[0]*(N+1)
ind=[0]*(N+1)
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    reverse_graph[b].append((a,c))
    ind[b]+=1
st,end=map(int,input().split())
res=[]
q=deque()
q.append(st)
while q:
    now=q.popleft()
    res.append(now)
    for i,cost in graph[now]:
        ind[i]-=1
        val[i]=max(val[i],val[now]+cost)
        if not ind[i]:
            q.append(i)

cnt=0
q.append(end)
while q:
    now=q.popleft()
    for i,cost in reverse_graph[now]:
        if val[now]==val[i]+cost:
            cnt+=1
            if not visit[i]:
                q.append(i)
                visit[i]=1
print(val[end])
print(cnt)