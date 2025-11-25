N=int(input())
li=[list(map(int,input().split())) for i in range(N)]

res=10**9
for i in range(1,1<<N):
    a,b=1,0
    for j in range(N):
        if i&(1<<j)!=0:
            a*=li[j][0]
            b+=li[j][1]
    res=min(res,abs(a-b))
print(res)