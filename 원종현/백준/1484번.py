G=int(input())
li=[i for i in range(1,50001)]
res=[]
s,t=0,0
while s<=t and t<len(li):
    now=li[t]**2-li[s]**2
    if now==G:
        res.append(li[t])
        t+=1
    elif now<G:
        t+=1
    else:
        s+=1
if res:
    print(*res,sep="\n")
else:
    print(-1)