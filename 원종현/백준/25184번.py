N=int(input())
if N==1:
    print(1)
else:
    res=[]
    for i in range(1,N//2+1):
        res.append(str(N//2+i))
        res.append(str(i))
    if N%2==1:
        res.append(str(N))
    print(' '.join(res))