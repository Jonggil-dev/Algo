N=int(input())
res=[]
for _ in range(N):
    S=input()
    tmp=''
    for i in S:
        if i.isdigit():
            tmp+=i
        else:
            if tmp!='':
                res.append(int(tmp))
                tmp=''
    if tmp!='':
        res.append(int(tmp))
res.sort()
print(*res,sep='\n')