li=list(map(int,input().split()))
res,tmp=0,[]
for i in li:
    a,b=i//3,i%3
    res+=a
    if b:
        tmp.append(b)
if len(tmp)==1:
    res+=1
elif len(tmp)>1:
    res+=max(tmp)
print(res)