N=int(input())
li=list(map(int,input().split()))
res=0
def func(now,tmp):
    global res
    if len(tmp)==0:
        res=max(res,now)
        return
    for i in range(len(tmp)):
        t=(tmp[i-1] if i!=0 else 0)*(tmp[i+1] if i+1!=len(tmp) else 0)
        func(now+t,tmp[:i]+tmp[i+1:])
func(0,li)
print(res)