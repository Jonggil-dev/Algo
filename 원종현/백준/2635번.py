N=int(input())
res=[]
for i in range(1,N+1):
    li=[N]
    li.append(i)

    idx=1
    while True:
        tmp=li[idx-1]-li[idx]
        if tmp<0:
            break
        li.append(tmp)
        idx+=1
    if len(res)<len(li):
        res=li
print(len(res))
print(*res)