N=int(input())
st,end=0,N
while st<=end:
    mid=(st+end)//2
    if mid**2<N:
        st=mid+1
    else:
        end=mid-1
print(st)