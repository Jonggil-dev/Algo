N=int(input())
mp,mf,ms,mv=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]
res=10**9
res2=[]
def func(m,idx,l):
    global res,res2
    if mp<=m[0] and mf<=m[1] and ms<=m[2] and mv<=m[3]:
        if res>m[4]:
            res=m[4]
            res2=[l]
        elif res==m[4]:
            res2.append(l)
        return
    if idx==N:
        return
    for i in range(idx,N):
        func([m[0]+li[i][0],m[1]+li[i][1],m[2]+li[i][2],m[3]+li[i][3],m[4]+li[i][4]],i+1,l+[i+1])

func([0,0,0,0,0],0,[])

if res!=10**9:
    print(res)
    print(*sorted(res2)[0])
else:
    print(-1)