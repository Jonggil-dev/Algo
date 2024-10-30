from collections import deque
import sys,math
input=sys.stdin.readline

N=int(input())
graph=[[]for _ in range(N+1)]
depth=[0]*(N+1)
log=int(math.log2(N))+1
log=20
for _ in range(N-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

parent=[[0]*2 for _ in range(N+1)]
visit=[0]*(N+1)
dp=[[[0]*3 for _ in range(log)] for _ in range(N+1)]

q=deque()
q.append(1)
visit[1]=1
while q:
    now=q.popleft()
    for next,cost in graph[now]:
        if not visit[next]:
            q.append(next)
            depth[next]=depth[now]+1
            visit[next]=1
            parent[next]=[now,cost]

for i in range(N+1):
    dp[i][0][0]=parent[i][0]
    dp[i][0][1]=parent[i][1]
    dp[i][0][2]=parent[i][1]

for i in range(1,log):
    for j in range(1,N+1):
        dp[j][i][0]=dp[dp[j][i-1][0]][i-1][0]
        dp[j][i][1]=min(dp[j][i-1][1],dp[dp[j][i-1][0]][i-1][1])
        dp[j][i][2]=max(dp[j][i-1][2],dp[dp[j][i-1][0]][i-1][2])

K=int(input())
for _ in range(K):
    a,b=map(int,input().split())
    if depth[a]<depth[b]:
        a,b=b,a
    diff=depth[a]-depth[b]
    res=[10**9,0]
    for i in range(log):
        if diff&1<<i:
            res[0]=min(res[0],dp[a][i][1])
            res[1]=max(res[1],dp[a][i][2])
            a=dp[a][i][0]
    if a==b:
        print(*res)
        continue
    for i in range(log-1,-1,-1):
        if dp[a][i][0]!=dp[b][i][0]:
            res[0]=min(res[0],dp[a][i][1],dp[b][i][1])
            res[1]=max(res[1],dp[a][i][2],dp[b][i][2])
            a=dp[a][i][0]
            b=dp[b][i][0]
    res[0]=min(res[0],dp[a][0][1],dp[b][0][1])
    res[1]=max(res[1],dp[a][0][2],dp[b][0][2])
    print(*res)

