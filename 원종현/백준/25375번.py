import sys
input=sys.stdin.readline

N=int(input())
for i in range(N):
    a,b=map(int,input().split())
    if b%a==0 and b//a>=2:
        print(1)
    else:
        print(0)
