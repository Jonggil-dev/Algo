N=int(input())
li=list(map(int,input().split()))
res=0
le,ri=0,N-1
while le<=ri:
    now=(ri-le-1)*min(li[le],li[ri])
    res=max(res,now)
    if li[le]<li[ri]:
        le+=1
    else:
        ri-=1
print(res)