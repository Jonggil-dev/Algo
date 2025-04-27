import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li=list(map(int,input().split()))

tmp=[0]*(N+1)
for i in range(1,N+1):
    tmp[i]=tmp[i-1]+li[i-1]
res=[tmp[i]-tmp[i-M] for i in range(M,N)]
print(max(res))