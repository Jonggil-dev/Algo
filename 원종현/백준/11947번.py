for _ in range(int(input())):
    N=input()
    s=5*(10**(len(N)-1))-1
    r1,r2='',''
    if int(N)>=s:
        r1=s+1
        r2=s
    else:
        r1=int(N)
        for i in N:
            r2+=str(9-int(i))
        r2=int(r2)
    print(r1*r2)