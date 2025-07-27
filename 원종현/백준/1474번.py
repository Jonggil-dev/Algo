import sys

input=sys.stdin.readline
N,M=map(int,input().split())
li=[input().rstrip() for i in range(N)]
l,r=divmod(M-sum(map(len,li)),N-1)
res=li[0]

for i in range(1,N):
    if li[i][0].islower() and r!=0:
        r-=1
        res+='_'*(l+1)+li[i]
    elif i+r==N:
        r-=1
        res+='_'*(l+1)+li[i]
    else:
        res+='_'*l+li[i]
print(res)