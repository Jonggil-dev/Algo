from collections import deque
N,W,L=map(int,input().split())
li=list(map(int,input().split()))[::-1]

q=deque()
t=0
l=0
while q or li:
    if q:
        a,b=q.pop()
        if t-b!=W:
            q.append((a,b))
        else:
            l-=a
    if li:
        now=li[-1]
        if l+now<=L:
            q.appendleft((li.pop(),t))
            l+=now
    t+=1

print(t)