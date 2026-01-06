from collections import deque
N=int(input())
D=list(map(int,input().split()))
H=list(map(int,input().split()))
q=deque([i for i in range(N)])

while len(q)>1:
    dps=0
    for i in range(len(q)):
        now=q.popleft()
        if H[now]-dps>0:
            dps+=D[now]
            q.append(now)
    for i in range(len(q)):
        now=q.popleft()
        H[now]-=dps-D[now]
        if H[now]>0:
            q.append(now)
print(q[0]+1)
