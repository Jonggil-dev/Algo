import sys
from collections import deque,defaultdict
input=sys.stdin.readline

N=int(input())
d=defaultdict(list)
for i in range(N-1):
    a,b,c=map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))
dist=[0]*(N+1)
q=deque()
q.append(1)

while q:
    now=q.popleft()
    for i in d[now]:
        if dist[i[0]]>0:
            continue
        dist[i[0]]=dist[now]+i[1]
        q.append(i[0])
print(max(dist))