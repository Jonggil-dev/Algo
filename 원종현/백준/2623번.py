from collections import deque
N,M=map(int,input().split())
li=[]
graph=[[] for _ in range(N+1)]
deg=[0]*(N+1)
for i in range(M):
    tmp=list(map(int,input().split()))
    for j in range(1,tmp[0]):
        st=tmp[j]
        end=tmp[j+1]
        graph[st].append(end)
        deg[end]=deg[end]+1
res=[]
q=deque()
for i in range(1,N+1):
    if deg[i]==0:
        q.append(i)
while q:
    now=q.popleft()
    res.append(now)
    for i in graph[now]:
        deg[i]-=1
        if not deg[i]:
            q.append(i)
if len(res)!=N:
    print(0)
else:
    for i in res:
        print(i)

