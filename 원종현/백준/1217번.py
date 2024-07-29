import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**7)
def func(now):
    global id, scc_id
    visit[now]=id
    parent=id
    id+=1
    stk.append(now)
    for next in graph[now]:
        if not visit[next]:
            parent=min(parent,func(next))
        if not finish[next]:
            parent=min(parent,visit[next])

    if parent==visit[now]:
        while stk:
            top=stk.pop()
            scc_idx[top]=scc_id
            finish[top]=1
            if now==top:
                break
        scc_id+=1
    return parent
while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    visit=[0]*(2*M+1)
    finish=[0]*(2*M+1)
    graph=[[] for _ in range(2*M+1)]
    stk=[]
    scc_idx=[0]*(2*M+1)
    id=1
    scc_id=1
    for i in range(N):
        a,b=map(int,input().split())
        graph[a].append(-b)
        graph[b].append(-a)
    for i in range(1,M+1):
        if not visit[i]:
            func(i)
    for i in range(1,M+1):
        if scc_idx[i]==scc_idx[-i]:
            print(0)
            break
    else:
        print(1)