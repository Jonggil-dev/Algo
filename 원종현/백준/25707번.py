N=int(input())
li=list(map(int,input().split()))
li.sort()
li=li+[li[0]]
now=li[0]
res=0
for i in li:
    res+=abs(i-now)
    now=i
print(res)