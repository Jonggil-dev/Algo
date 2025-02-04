import sys
input=sys.stdin.readline

while True:
    N,M=map(int,input().split())
    res=0
    if N==0 and M==0:
        break
    check={}
    for i in range(N):
        a=int(input())
        check[a]=1
    for i in range(M):
        a=int(input())
        if a in check:
            res+=1
    print(res)
