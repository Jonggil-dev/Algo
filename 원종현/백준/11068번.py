N=int(input())

for i in range(N):
    now=int(input())
    res=[]
    for j in range(2,65):
        li=[]
        tmp=now
        while tmp!=0:
            li.append(tmp%j)
            tmp//=j

        for k in range(len(li)//2):
            if li[k]!=li[-k-1]:
                res.append('X')
                break
    print(1 if len(res)!=63 else 0)