from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
graph=[[] for _ in range(N+1)]
parent=[0]*(N+1)
visit=[0]*(N+1)
depth=[0]*(N+1)

for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q=deque()
q.append(1)
visit[1]=1
while q:
    now=q.popleft()
    for next in graph[now]:
        if visit[next]:continue
        visit[next]=1
        depth[next]=depth[now]+1
        parent[next]=now
        q.append(next)
dp=[[0]*(20)for _ in range(N+1)]
for i in range(N+1):
    dp[i][0]=parent[i]

for i in range(1,20):
    for j in range(1,N+1):
        dp[j][i]=dp[dp[j][i-1]][i-1]
course=[]
M=int(input())
for i in range(M):
    now=int(input())
    if i==0:
        course.append([now,now])
        continue
    course.append([course[-1][1],now])
course.pop(0)
def lca(x,y):
    if depth[x]<depth[y]:
        x,y=y,x
    diff=depth[x]-depth[y]
    for i in range(20):
        if diff&1<<i:
            x=dp[x][i]
    if x==y:
        return x
    for i in range(20-1,-1,-1):
        if dp[x][i]!=dp[y][i]:
            x=dp[x][i]
            y=dp[y][i]
    return dp[x][0]
#print(course)
res=0
for a,b in course:
    c=lca(a,b)
    print(a,b,c)
    res+=depth[a]+depth[b]-2*depth[c]
print(res)