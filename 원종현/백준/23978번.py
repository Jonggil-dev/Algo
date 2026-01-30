N,K=map(int,input().split())
li=list(map(int,input().split()))
st,end=0,K+1
while st<end-1:
    mid=(st+end)//2
    res=(mid*(mid+1))//2
    for i in range(N-1):
        diff=li[i+1]-li[i]
        if diff>=mid:
            res+=(mid*(mid+1))//2
        else:
            res+=(2*mid-diff+1)*diff//2
    if res>=K:
        end=mid
    else:
        st=mid
print(end)