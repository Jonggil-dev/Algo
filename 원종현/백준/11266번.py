import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
V,E=map(int,input().split())
visit=[0]*(V+1)
check=[0]*(V+1)
graph=[[] for _ in range(V+1)]
for _ in range(E):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

res=set()
count=0
def func(st,end):
    global count
    count+=1
    visit[st]=True
    check[st]=count
    now=check[st]
    child_count=0
    for child in graph[st]:
        if child==end:
            continue
        if visit[child]:
            now=min(now,check[child])
            continue
        child_count+=1
        sub=func(child,st)
        now=min(now,sub)
        if sub>=check[st] and end!=0:
            res.add(st)
    if end==0 and child_count>1:
        res.add(st)
    return now
for i in range(1,V+1):
    if not visit[i]:
        func(i,0)
print(len(res))
print(*sorted(list(res)),sep=" ")