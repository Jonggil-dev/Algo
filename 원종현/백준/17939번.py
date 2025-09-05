N=int(input())
li=list(map(int,input().split()))

tmp=0
res=0
tmp2=0
maxNum=max(li)
for i in range(N):
    if li[i]<maxNum:
        tmp2+=li[i]
        tmp+=1
    else:
        res+=(maxNum*tmp-tmp2)
        if i!=(N-1):
            maxNum=max(li[i+1:])
        tmp=0
        tmp2=0
print(res)