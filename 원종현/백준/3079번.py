import sys
input=sys.stdin.readline
N,M=map(int,input().split())
li=[int(input()) for _ in range(N)]

l,r=min(li),max(li)*M
res=r

while l<=r:
    tot=0
    mid=(l+r)//2
    for i in range(N):
        tot+=mid//li[i]
    if tot>=M:
        r=mid-1
        res=min(mid,res)
    else:
        l=mid+1
print(res)