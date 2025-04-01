for _ in range(int(input())):
    s='\''+input()
    s=s.replace(':','\':').replace(',',',\'')
    d=eval('{'+s+'}')
    g=[[j for j in i.split('&')] for i in input().split('|')]
    res=10**9
    for i in g:
        t=0
        for j in i:
            t=max(t,d[j])
        res=min(res,t)
    print(res)