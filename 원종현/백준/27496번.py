from collections import deque
N,L=map(int,input().split())
li=list(map(int,input().split()))
q=deque()
now=0
res=0
for i in li:
    q.append(i)
    now+=i
    if len(q)>L:
        now-=q.popleft()
    if 129<=now<=138:
        res+=1
print(res)