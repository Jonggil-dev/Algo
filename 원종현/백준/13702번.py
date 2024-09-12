import sys
input=sys.stdin.readline

N,K=map(int,input().split())
li=sorted([int(input()) for _ in range(N)])
st,end=1,li[N-1]
res=0
while st<=end:
    mid=(st+end)//2
    tmp=0
    cnt=0
    for i in li:
        if not mid:
            continue
        cnt+=i//mid
    if cnt>=K:
        res=max(res,mid)
        st=mid+1
    elif cnt<K:
        end=mid-1

print(res)