N=int(input())
li=list(input())
res=0
tmp=[]
for i in li:
    if i in 'SL':
        tmp.append(i)
    elif i=='K':
        if 'S' in tmp:
            tmp.remove('S')
            res+=1
        else:
            break
    elif i=='R':
        if 'L' in tmp:
            tmp.remove('L')
            res+=1
        else:
            break
    else:
        res+=1
print(res)