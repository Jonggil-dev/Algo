N=int(input())
if N==0:
    print(0)
elif N==1:
    print(4)
else:
    r=0
    res=0
    while pow(r,2)<N:
        r+=1
    if (r-1)*r>N:
        res=(r-2+r-1)*2
    else:
        res=(r-1)*4
    print(res)