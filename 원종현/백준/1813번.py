N=int(input())
li=list(map(int,input().split()))
res=-1
for i in range(N+1):
    tmp=li.count(i)
    if tmp==i:
        res=max(res,i)
print(res)