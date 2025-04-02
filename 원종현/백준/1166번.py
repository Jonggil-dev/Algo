N,L,W,H=map(int,input().split())
res=0
st,end=0,min([L,W,H])+1
for _ in range(10000):
    mid=(st+end)/2
    c=(L//mid)*(W//mid)*(H//mid)
    if c>=N:
        res=max(res,mid)
        st=mid
    else:
        end=mid
print(res)