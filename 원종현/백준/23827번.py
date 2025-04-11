N=int(input())
li=list(map(int,input().split()))
tmp=sum(li)
res=0
for i in li:
    tmp-=i
    res=(res+i*tmp)%1000000007
print(res)