N=int(input())
res=0
li=[list(map(int,input().split())) for i in range(N)]
li.sort()
print(li)
for a,b in li:
    if res>a:
        res+=b
    else:
        res=a+b
print(res)