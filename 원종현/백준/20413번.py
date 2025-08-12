N=int(input())
s,g,p,d=map(int,input().split())
li=input()

res=[0]
for i in li:
    bp,sp,gp,pp,dp=s-res[-1]-1,g-res[-1]-1,p-res[-1]-1,d-res[-1]-1,d
    if i=='B':
        res.append(bp)
    elif i=='S':
        res.append(sp)
    elif i=='G':
        res.append(gp)
    elif i=='P':
        res.append(pp)
    else:
        res.append(dp)
print(sum(res))