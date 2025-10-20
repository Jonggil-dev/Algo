
def func(x):
    global visit,d
    if x in visit:
        return 0
    visit[x]=1

    for y in new_li:
        if x+y in so:
            if y not in d or func(d[y]):
                d[y]=x
                return 1
    return 0

so=[]
for i in range(2,2001):
    check=1
    for j in range(2,i):
        if i%j==0:
            check=0
            break
    if check:
        so.append(i)

N=int(input())
li=list(map(int,input().split()))


res=[]
for i in li[1:]:
    d={}

    if li[0]+i in so:
        if N==2:
            res.append(i)
            break
        new_li=[j for j in li if j not in [li[0],i]]
        for x in new_li:
            visit={}
            func(x)
            print(f'd:{d},|||| v:{visit}')
    if N!=2 and len(d)==N-2:
        res.append(i)
        print(d)
res.sort()
print(' '.join(list(map(str,res))) if res else -1)
