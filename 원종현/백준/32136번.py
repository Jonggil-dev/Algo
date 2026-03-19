N=int(input())
li=list(map(int,input().split()))


st,end=0,300000*500000
res=end

while st<=end:
    mid=(st+end)//2

    st_max,end_min=0,N-1
    for i in range(N):
        dist=mid//li[i]
        st_max=max(st_max,i-dist)
        end_min=min(end_min,i+dist)
        if st_max>end_min:
            break
    if st_max<=end_min:
        res=mid
        end=mid-1
    else:
        st=mid+1
print(res)