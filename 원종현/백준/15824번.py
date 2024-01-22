import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int,input().split()))
li.sort()
r,d=0,1000000007
for i in range(N):
    r+=(pow(2,i,d)-pow(2,N-i-1,d))*li[i]
print(r%d)