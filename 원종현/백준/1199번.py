import sys
input=sys.stdin.readline


N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]
graph=[{} for _ in range(N)]
for i in range(N):
    deg=0
    for j in range(N):
        deg+=li[i][j]
        if li[i][j]:
            graph[i][j]=li[i][j]
    if deg%2:
        print(-1)
        exit()

stk=[]
stk.append(0)
res=[]
while stk:
    now=stk.pop()
    if graph[now]:
        for next,c in graph[now].items():
            graph[now][next]-=1
            graph[next][now]-=1
            if graph[now][next]==0:
                graph[now].pop(next)
                graph[next].pop(now)
            stk.append(now)
            stk.append(next)
            break
    else:
        res.append(now+1)
print(*res)
