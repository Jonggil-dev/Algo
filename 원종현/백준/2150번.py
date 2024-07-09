import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

V,E=map(int,input().split())

graph=[[] for _ in range(V+1)]
parents=[-1]*(V+1)
for _ in range(E):
    a,b=map(int,input().split())
    graph[a].append(b)


stk=[]
visit=[0]*(V+1)
id=0
res=[]
def func(now):
    global id
    id+=1
    parents[now]=id
    stk.append(now)
    visit[now]=1
    parent=parents[now]

    for next in graph[now]:
        if parents[next]==-1:
            parent=min(parent,func(next))
        elif visit[next]:
            parent=min(parent,parents[next])

    if parent==parents[now]:
        scc=[]
        while True:
            node=stk.pop()
            visit[node]=0
            scc.append(node)
            if now==node:
                break
        res.append(sorted(scc)+[-1])
    return parent

for i in range(1,V+1):
    if parents[i]==-1:
        func(i)
res.sort()
print(len(res))
for i in res:
    print(*i)