import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
N,M=map(int,input().split())
status=[0]+list(map(int,input().split()))
room=[[] for _ in range(N+1)]
graph=[[] for _ in range(2*M+1)]
for i in range(1,M+1):
    K,*tmp=map(int,input().split())
    for j in tmp:
        room[j].append(i)

for i in range(1,N+1):
    a,b=room[i]
    if status[i]:
        graph[a].append(b)
        graph[-b].append(-a)
        graph[-a].append(-b)
        graph[b].append(a)
    else:
        graph[-a].append(b)
        graph[-b].append(a)
        graph[a].append(-b)
        graph[b].append(-a)

finish=[0]*(2*M+1)
visit=[0]*(2*M+1)
scc_idx=[0]*(2*M+1)
id=1
scc_id=1
stk=[]
def func(now):
    global id,scc_id
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
        print(0)
        break
else:
    print(1)
