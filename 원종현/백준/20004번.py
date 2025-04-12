import sys
input=sys.stdin.readline

N=int(input())
for i in range(1,N+1):
    tmp=i+1
    if 30%tmp==0:
        print(i)