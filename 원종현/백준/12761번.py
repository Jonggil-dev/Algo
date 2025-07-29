from collections import deque

A,B,N,M=map(int,input().split())
graph=[-1]*(100001)
q=deque()
q.append(N)
graph[N]=0
chk=0
while q:
    now=q.popleft()
    for i in [now-1,now+1,now+A,now-A,now+B,now-B,now*A,now*B]:
        if 0<=i<=100000 and graph[i]==-1:
            q.append(i)
            graph[i]=graph[now]+1
            if i==M:
                chk=1
                break
    if chk:
        break
print(graph[M])