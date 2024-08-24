import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M=map(int,input().split())
graph=[[] for _ in range(2*M+1)]
for i in range(N):
    x,y=map(int,input().split())
    graph[-x].append(y)
    graph[-y].append(x)

visit=[0]*(2*M+1)
finish=[0]*(2*M+1)
scc_idx=[0]*(2*M+1)
stk=[]
id=1
scc_id=1

def func(now):
    global id, scc_id
    visit[now]=id
    parent=id
    id+=1
    stk.append(now)
    for next in graph[now]:
        if not visit[next]:
            parent=min(parent,func(next))
        elif not finish[next]:
            parent=min(parent,visit[next])

    if parent==visit[now]:
        while stk:
            top=stk.pop()
            finish[top]=1
            scc_idx[top]=scc_id
            if top==now:
                break
        scc_id+=1
    return parent

for i in range(1,2*M+1):
    if not visit[i]:
        func(i)

for i in range(1,M+1):
    if scc_idx[i]==scc_idx[-i]:
        print("OTL")
        break
else:
    print("^_^")