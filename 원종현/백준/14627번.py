import sys
input=sys.stdin.readline
S,C=map(int,input().split())
li=sorted([int(input()) for _ in range(S)])
res=0
st,end=1,li[-1]
while st<=end:
    mid=(st+end)//2
    cnt=0
    for i in li:
        cnt+=i//mid
    if cnt>=C:
        res=max(res,mid)
        st=mid+1
    else:
        end=mid-1
print(sum(li)-C*res)