import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

N,M=map(int,input().split())
graph=[[] for _ in range(N*2+1)]
for i in range(M):
    x,y=map(int,input().split())
    graph[-x].append(y)
    graph[-y].append(x)

stk=[]
visit=[0]*(2*N+1)
parents=[-1]*(2*N+1)
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
        res.append(scc)
    return parent
for i in range(1,N+1):
    if not visit[i]:
        func(i)
r=1
for scc in res:
    if r==0:
        break
    tmp=set()
    for i in scc:
        if -i in tmp:
            r=0
            break
        tmp.add(i)
print(r)