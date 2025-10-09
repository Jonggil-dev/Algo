d,li={},[]
for i in range(12):
    x,y=map(int,input().split())
    if x in d:
        d[x].append(y)
    else:
        d[x]=[y]
    if y in d:
        d[y].append(x)
    else:
        d[y]=[x]
for i in d:
    if len(d[i])==3:
        li.append(i)
for i in li:
    res=0
    for j in d[i]:
        res+=len(d[j])
    if res==6:
        print(i)
        break