import sys

input=sys.stdin.readline
N,K=map(int,input().split())
res=set()

def func(v,a):
    if v==N:
        res.add(tuple(a))
        return
    if v+1<=N:
        func(v+1,a+[1])
    if v+2<=N:
        func(v+2,a+[2])
    if v+3<=N:
        func(v+3,a+[3])

func(0,[])
if len(res)<K:
    print(-1)
else:
    res=list(res)
    res.sort()
    res=res[K-1]
    print(*res,sep="+")
