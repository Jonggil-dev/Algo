import sys
input=sys.stdin.readline
while True:
    N=int(input())
    if N==0:
        break
    li=[int(input()) for _ in range(N)]
    for i in range(1,N):
        li[i]=max(li[i],li[i]+li[i-1])
    print(max(li))