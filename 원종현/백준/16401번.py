M,N=map(int,input().split())
L=list(map(int,input().split()))

st,end=1,10**9
res=0
while st<=end:
    mid=(st+end)//2
    tmp=0
    for i in L:
        tmp+=i//mid
    if tmp>=M:
        res=max(res,mid)
        st=mid+1
    else:
        end=mid-1
print(res)