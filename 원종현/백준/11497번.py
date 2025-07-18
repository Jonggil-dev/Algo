import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    li.sort()
    res=0
    for i in range(2,N):
        res=max(res,abs(li[i]-li[i-2]))
    print(res)