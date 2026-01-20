N=int(input())
st,end=1,N*5

res=10**9

def func(x):
    cnt=0
    while x>=5:
        cnt+=x//5
        x//=5
    return cnt

while st<=end:
    mid=(st+end)//2
    tmp=func(mid)
    if tmp<N:
        st=mid+1
    elif tmp>=N:
        if tmp==N:
            res=mid
        end=mid-1
print(-1 if res==10**9 else res)