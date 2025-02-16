for _ in range(int(input())):
    N=int(input())
    res=0
    while N!=6174:
        res+=1
        tmp=list(str(N))
        N=int(''.join(sorted(tmp,reverse=True)))-int(''.join(sorted(tmp)))
        if N<1000:
            strN=str(N)
            for _ in range(4-len(strN)):
                strN+='0'
            N=int(strN)
    print(res)