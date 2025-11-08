K=int(input())
li=[2**i for i in range(21)]
tmp=0
for i in li:
    if K<=i:
        tmp=i
        break
res=0
tmp2=tmp
if K!=tmp:
    while K:
        tmp2//=2
        if K>=tmp2:
            K-=tmp2
        res+=1
print(tmp,res)