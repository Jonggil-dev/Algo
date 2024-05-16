N,M=map(int,input().split())
if not N:
    print(0)
else:
    li=list(map(int,input().split()))
    tar=0
    res=1
    for i in range(N-1,-1,-1):
        tar+=li[i]
        if tar>M:
            res+=1
            tar=li[i]
    print(res)