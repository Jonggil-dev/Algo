import sys
input=sys.stdin.readline

N=int(input())
K=int(input())
li=list(map(int,input().split()))
li.sort()

if K>=N:
    print(0)
else:
    tmp=[0]
    for i in range(1,N):
        tmp.append(li[i]-li[i-1])
    tmp.sort()
    print(sum(tmp[:N-K+1]))
