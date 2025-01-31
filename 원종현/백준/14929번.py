N=int(input())
li=list(map(int,input().split()))
pre=0
res=0
for i in range(len(li)-1):
    pre+=li[i]
    res+=li[i+1]*pre
print(res)