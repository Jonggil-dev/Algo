import sys
input=sys.stdin.readline

N=int(input())
li=list(map(int,input().split()))
k=int(input())

for i in range(0,N,N//k):
    tmp=li[i:i+N//k]
    tmp.sort()
    print(*tmp,end=" ")