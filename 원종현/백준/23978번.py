import sys
input=sys.stdin.readline

N,K=map(int,input().split())
li=list(map(int,input().split()))
st,end=1,10**18
while st<=end:
    mid=(st+end)//2
    res=0
    for i in range(1,N):
        v=mid-(li[i]-li[i-1]-1)
        if v>=0:
            res+=(mid+v)*(1+mid-v)//2
        else:
            res+=mid*(mid+1)//2
    res+=mid*(mid+1)//2
    if res>=K:
        end=mid-1
    else:
        st=mid+1
print(st)