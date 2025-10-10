N=int(input())
res=0
while N:
    S=str(N)
    res+=S.count("1")
    N=int("0"+S.replace("1",""))
    if N:
        N-=1
        res+=1
print(res)