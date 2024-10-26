from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
q=deque()
while True:
    now=int(input())
    if now==-1:
        break
    if now and len(q)<N:
        q.append(now)
    elif not now:
        q.popleft()

if q:
    print(*q)
else:
    print('empty')