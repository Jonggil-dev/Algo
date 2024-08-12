for i in range(int(input())):
    input()
    r,c=map(int,input().split())
    res=0
    t=['' for _ in range(c)]
    for i in range(r):
        tmp=input()
        res+=tmp.count('>o<')
        for j in range(c):
            t[j]+=tmp[j]
    for i in t:
        res+=i.count('vo^')
    print(res)