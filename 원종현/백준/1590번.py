N,T=map(int,input().split())
res=[]

for i in range(N):
    S,I,C=map(int,input().split())
    t=[S+(I*c) for c in range(C)]
    if t[-1]<T:
        continue

    st,end=0,C-1
    tmp=0
    while st<=end:
        mid=(st+end)//2
        if t[mid]>=T:
            tmp=mid
            end=mid-1
        else:
            st=mid+1
    res.append(t[tmp]-T)

print(min(res) if res else -1)