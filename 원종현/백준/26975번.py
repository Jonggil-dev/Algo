N=int(input())
li=list(map(int,input().split()))
li.sort(reverse=True)
res1,res2=0,0
for i in range(N):
    tmp=li[i]*(i+1)
    if tmp>=res1:
        res1=tmp
        res2=li[i]
print(res1,res2)