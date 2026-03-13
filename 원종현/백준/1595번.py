from collections import deque
import sys
input=sys.stdin.readline

def func(st):
    q=deque()
    q.append((st,0))
    visit=[0]*(10001)
    visit[st]=1
    max_cost=0
    tar=0
    while q:
        now,c=q.popleft()
        for next,next_cost in graph[now]:
            cost=c+next_cost
            if not visit[next]:
                visit[next]=1
                q.append((next,cost))
                if max_cost<cost:
                    max_cost=cost
                    tar=next
    return (tar,max_cost)

cnt=0
graph=[[] for _ in range(10001)]
min_v=10**9
try:
    while True:
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
        cnt+=1
        min_v=min(min_v,a,b)
except:
    pass

if not cnt:
    print(0)
else:
    print(func(func(min_v)[0])[1])