import sys
input=sys.stdin.readline


N=int(input())
li=list(map(int,input().split()))
tmp=0
res=0
for i in range(N-1,-1,-1):
    tmp=max(tmp,li[i])
    res=max(res,tmp-li[i])
print(res)