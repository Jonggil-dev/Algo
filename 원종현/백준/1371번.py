d={}
try:
    while True:
        tmp=input().split()
        for i in tmp:
            for j in range(len(i)):
                if i[j] in d:
                    d[i[j]]+=1
                else:
                    d[i[j]]=1
except:
    pass
r=sorted([(k,v) for k,v in d.items()],key=lambda x:(x[1]),reverse=True)
res=[]
for k,v in r:
    if v==r[0][1]:
        res.append(k)
print(*sorted(res))