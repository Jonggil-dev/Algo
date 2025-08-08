import sys
input=sys.stdin.readline

N,K=map(int,input().split())
li=list(map(int,input().split()))
D=list(map(int,input().split()))
for i in range(K):
    tmp=[0]*N
    for j in range(N):
        tmp[D[j]-1]=li[j]
    li=tmp
print(*li)