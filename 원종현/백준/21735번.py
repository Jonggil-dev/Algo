N,M=map(int,input().split())
li=list(map(int,input().split()))
res=0
def func(t,idx,v):
    global res
    v+=li[idx]
    if t==M or idx==N-1:
        res=max(res,v)
        return
    if idx+1<N:
        func(t+1,idx+1,v)
    if idx+2<N:
        func(t+1,idx+2,v//2)
func(1,0,1)
if N>1:
    func(1,1,0)
print(res)