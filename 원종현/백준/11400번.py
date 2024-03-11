import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
V,E=map(int,input().split())
graph=[[]for _ in range(V+1)]
visit=[0]*(V+1)
check=[0]*(V+1)
for _ in range(E):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
res=[]
c=1
def func(st,pa):
    global c
    c+=1
    visit[st]=True
    check[st]=c
    now=check[st]
    for child in graph[st]:
        if child==pa:
            continue
        if visit[child]:
            now=min(now,check[child])
            continue
        sub=func(child,st)
        now=min(sub,now)
        if sub>check[st]:
            res.append(sorted([st,child]))
    return now
func(1,0)
res.sort()
print(len(res))
for a,b in res:
    print(a,b)