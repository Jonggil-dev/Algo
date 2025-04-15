for _ in range(int(input())):
    N=int(input())
    A=input().split()
    B=input().split()
    C=input().split()
    res=['']*(N)
    d={}
    t=0
    for i in B:
        d[A.index(i)]=C[t]
        t+=1
    for k,v in d.items():
        res[k]=v
    print(*res)