import sys
input=sys.stdin.readline

N,M,L=map(int,input().split())
li=sorted([0]+list(map(int,input().split()))+[L])

dists=[li[i+1]-li[i] for i in range(len(li)-1)]
st,end=1,L
res=0
while st<=end:
    cnt=0
    mid=(st+end)//2
    for dist in dists:
        if dist>mid:
            cnt+=(dist-1)//mid
    if cnt<=M:
        res=mid
        end=mid-1
    else:
        st=mid+1
print(res)
