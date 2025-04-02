N,F=map(int,input().split())

def func(li):
    if len(li)==1:
        return li[0]
    t=func([li[i]+li[i+1] for i in range(len(li)-1)])
    return t
res=[]
def go(now):
    global res
    if res:
        return
    if len(now)==N:
        if func(now)==F:
            res=now
        return
    for i in range(1,N+1):
        if i not in now:
            go(now+[i])
go([])
print(res)