from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li=[list(map(int,input().split())) for i in range(M)]
q=deque([(0,0)])

while q:
    r,c=q.popleft()
    for i in [(0,1),(1,0)]:
        dr=r+i[0]
        dc=c+i[1]
        if 0<=dr<M and 0<=dc<N and li[dr][dc]==1:
            li[dr][dc]+=li[r][c]
            q.append((dr,dc))

if li[M-1][N-1]+1==N+M:
    print('Yes')
else:
    print('No')