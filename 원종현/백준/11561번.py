for i in range(int(input())):
    N=int(input())
    st,end=1,N
    res=0
    while st<=end:
        mid=(st+end)//2
        if ((mid+1)*mid)//2<=N:
            st=mid+1
            res=mid
        else:
            end=mid-1
    print(res)