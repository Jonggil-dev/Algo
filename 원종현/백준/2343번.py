N,M=map(int,input().split())
li=list(map(int,input().split()))

st=max(li)
end=sum(li)
def func(mid):
    c=0
    now=0
    for i in range(N):
        now+=li[i]
        if now>mid:
            c+=1
            now=li[i]
    if now:
        c+=1
    return c
while st<=end:
    mid=(st+end)//2
    co=func(mid)
    print(st,end,mid,co)
    if co<=M:
        end=mid-1
    else:
        st=mid+1
print(st)