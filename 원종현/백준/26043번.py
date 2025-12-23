from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
q=deque()
A,B,C=[],[],[]
for i in range(N):
    S=input().rstrip().split()
    if S[0]=='1':
        q.append((S[1],int(S[2])))
    else:
        if q:
            a,b=q.popleft()
            c=int(S[1])
            if b==c:
                A.append(a)
            else:
                B.append(a)
C=[i for i,_ in q]
A.sort(key=int)
B.sort(key=int)
C.sort(key=int)

print('None' if not A else ' '.join(A))
print('None' if not B else ' '.join(B))
print('None' if not C else ' '.join(C))