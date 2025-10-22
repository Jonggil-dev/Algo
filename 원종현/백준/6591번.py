import sys
input=sys.stdin.readline

while True:
    N,K=map(int,input().split())
    if N==0 and K==0:
        break
    a,b=1,1
    for i in range(N,max(K,N-K),-1):
        a*=i
    for i in range(1,min(N-K,K)+1):
        b*=i
    print(a//b)