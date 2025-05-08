from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
q=deque()
chk=[]
for _ in range(N):
    li=input().rstrip().split()
    if li[0]=='1':
        q.append(li[1])
        chk.append(-1)
    elif li[0]=='2':
        q.appendleft(li[1])
        chk.append(1)
    else:
        if not q:
            continue
        if chk[-1]==1:
            q.popleft()
            chk.pop()
        else:
            q.pop()
            chk.pop()

if q:
    print(*q,sep="")
else:
    print(0)