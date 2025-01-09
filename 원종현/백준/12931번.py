N=int(input())
li=sorted(list(map(int,input().split())))

res=0
while sum(li)!=0:
    tmp=0
    for i in range(N):
        if li[i]%2!=0 or li[i]==0 or li[i]==1:
            if li[i]==0:
                continue
            else:
                li[i]-=1
                res+=1
            tmp=1
    if tmp==0:
        for i in range(N):
            li[i]//=2
        res+=1
print(res)
