N,m,M,T,R=map(int,input().split())

now=m
if m+T>M:
    print(-1)
else:
    cnt=0
    res=0
    while cnt<N:
        if now+T<=M:
            now+=T
            cnt+=1
        else:
            now=max(m,now-R)
        res+=1
    print(res)
