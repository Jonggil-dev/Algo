M,N=map(int,input().split())
li=list(map(int,input().split()))


st,end=0,max(li)
r=0
while st<=end:
    tot=0
    mid=(st+end)//2
    if not mid:
        tot=0
        break
    for i in li:
        if i>=mid:
            tot+=i//mid
    if tot>=M:
        st=mid+1
        r=mid
    else:
        end=mid-1
print(r)