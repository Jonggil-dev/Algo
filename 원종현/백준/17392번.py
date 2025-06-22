N,M=map(int,input().split())
li=list(map(int,input().split()))

if sum(li)>=M:
    res=0
else:
    m=M
    tmp,idx=0,0
    while m>0:
        tmp-=1
        if tmp<=-1:
            if idx<N:
                tmp=li[idx]
                idx+=1
            else:
                break
        m-=1
    cnt=m
    res=0
    tmp2,idx2=1,1
    while idx2<=cnt:
        for i in range(N+1):
            if idx2>cnt:
                break
            res+=tmp2**2
            idx2+=1
        tmp2+=1
print(res)