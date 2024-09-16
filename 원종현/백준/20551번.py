import sys
input=sys.stdin.readline

N,M=map(int,input().split())

li=sorted([int(input()) for i in range(N)])
d={}
for i in range(N):
    if li[i] not in d:
        d[li[i]]=i
for _ in range(M):
    D=int(input())
    if D in d:
        print(d[D])
    else:
        print(-1)
