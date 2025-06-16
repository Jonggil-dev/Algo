N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]
res=0
fair={0:5,1:3,2:4,3:1,4:2,5:0}
def func(n):
    tmp=0
    for i in range(N):
        for j in range(6):
            if li[i][j]==n:
                now=li[i][fair[j]]
                if 6 in [n,now]:
                    tmp+=4 if 5 in [n,now] else 5
                else:
                    tmp+=6
                n=now
                break
    return tmp
res=0
for i in range(1,7):
    res=max(res,func(i))
print(res)

