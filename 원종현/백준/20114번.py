def func(i):
    global res
    for j in range(W*i,W*(i+1)):
        for k in range(H):
            if li[k][j]!='?':
                res+=li[k][j]
                return
    res+='?'
    return
N,H,W=map(int,input().split())
li=[list(input()) for _ in range(H)]
res=''
for i in range(N):
    func(i)
print(res)