S=input()
res=[0,0,0]
f=S[0]

if S[0]=='U':
    if S[1]=='U':
        res[1]+=1
    else:
        res[1]+=1
        res[0]+=2
else:
    if S[1]=='U':
        res[0]+=1
        res[1]+=2
    else:
        res[0]+=1
res[0]+=S[2:].count('D')*2
res[1]+=S[2:].count('U')*2

for i in S:
    if f=='U':
        if i=='U':
            pass
        else:
            res[2]+=1
    else:
        if i=='U':
            res[2]+=1
        else:
            pass
    f=i
print(*res,sep="\n")