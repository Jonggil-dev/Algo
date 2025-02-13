P=int(input())
for _ in range(P):
    li=list(map(int,input().split()))
    res=0
    for i in range(1,len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
                res+=1
    print(li[0],res)