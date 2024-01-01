import sys,heapq
input=sys.stdin.readline
INF=float('inf')
V,E=map(int,input().split())
graph=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dtra(start,target=-1):
    q=[]
    heapq.heappush(q,(0,start))
    distance=[INF]*(V+1)
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for new_now,dis in graph[now]:
            cost=dist+dis
            if cost<distance[new_now]:
                distance[new_now]=cost
                heapq.heappush(q,(cost,new_now))
    if target==-1:
        return distance
    return distance[target]

st,*course=map(int,input().split())
comp2=dtra(int(input()))
time=0
comp=[INF]*(V+1)
comp[st]=0
res=-1
for i in course:
    c=dtra(st,i)
    if c==INF or st==i:
        continue
    st=i
    comp[i]=max(0 if comp[i]==INF else comp[i],c+time)
    time+=c
for i in range(1,V+1):
    if comp[i]>=comp2[i] and comp[i]!=INF:
        res=i
        break
print(res)