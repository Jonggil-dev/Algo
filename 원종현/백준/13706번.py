N=int(input())
st,end=1,N
while True:
    mid=(st+end)//2
    if mid**2==N:
        print(mid)
        break
    elif mid**2>N:
        end=mid-1
    else:
        st=mid+1