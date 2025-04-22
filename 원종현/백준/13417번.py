from collections import deque
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    li=input().split()
    q=deque()
    q.append(li[0])
    for i in li[1:]:
        if i>q[0]:
            q.append(i)
        else:
            q.appendleft(i)
    print(*q,sep="")