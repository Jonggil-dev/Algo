from collections import deque

N=int(input())
li=[input().split() for _ in range(N)]
q=deque(li)

while len(q)>1:
    a,b=q.popleft()
    for i in range(int(b)-1):
        q.append(q.popleft())
    q.popleft()
print(q[0][0])