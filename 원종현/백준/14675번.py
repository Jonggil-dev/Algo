import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(input())
graph=[[] for _ in range(N+1)]
visit=[0]*(N+1)
check=[0]*(N+1)
order=[[]]
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    order.append(sorted((a,b)))
c=0
r=set()
rp=set()
def func(st,end):
    global c
    c+=1
    check[st]=c
    visit[st]=True
    now=check[st]
    child=0
    for i in graph[st]:
        if i==end:
            continue
        if visit[i]:
            now=min(visit[i],now)
            continue
        child+=1
        sub=func(i,st)
        now=min(sub,now)
        if sub>check[st]:
            r.add((min(st,i),max(st,i)))
        if end!=0 and sub>=check[st]:
            rp.add(st)
    if end==0 and child>1:
        rp.add(st)

    return now
func(1,0)
for i in range(int(input())):
    a,b=map(int,input().split())
    if a==1:
        if b in rp:
            print("yes")
        else:
            print("no")
    else:
        if (order[b][0],order[b][1]) in r:
            print("yes")
        else:
            print("no")