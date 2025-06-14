N,M=map(int,input().split())
li=[int(input()) for _ in range(N)]
l,r=min(li),sum(li)
res=0
while l<=r:
    mid=(l+r)//2
    now=mid
    cnt=1
    for i in range(N):
        if now<li[i]:
            now=mid
            cnt+=1
        now-=li[i]
    if cnt>M or mid<max(li):
        l=mid+1
    else:
        r=mid-1
        res=mid
print(res)