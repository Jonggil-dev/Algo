N,M=map(int,input().split())
if N>M:
    print(0)
else:
    if N==1:
        print(1)
    else:
        res=1
        for i in range(2,N+1):
            res=(res*i)%M
        print(res)