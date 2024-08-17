N=int(input())
li=[]
ch=set()
for i in range(N):
    tmp=list(map(int,input().split()))
    li.append(tmp)
    ch=ch.union(set(tmp))
val=sum(li[0])
flag=0
if len(ch)==N**2:
    t1,t2=0,0
    ts=[0]*N
    for i in range(N):
        if sum(li[i])!=val:
            flag=1
            break
        t1+=li[i][i]
        t2+=li[i][N-1-i]
        for j in range(N):
            ts[j]+=li[i][j]
    if t1!=val or t2!=val:
        flag=1
    for i in ts:
        if i!=val:
            flag=1

else:
    flag=1


if flag:
    print("FALSE")
else:
    print("TRUE")