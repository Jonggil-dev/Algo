N=1
res=[]
while N:
    N=int(input())
    li=[input() for _ in range(N)]
    val=[]
    for i in range(2*N-1):
        val.append(int(input().split()[0]))
    val.sort()
    for i in range(0,len(val),2):
        if i==(len(val)-1) or val[i]!=val[i+1]:
            res.append(li[val[i]-1])
            break
for i in range(len(res)):
    print(i+1,res[i])