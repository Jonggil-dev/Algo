N,K=map(int,input().split())
A=list(map(int,input().split()))
res=0

def func(t,v):
    global res
    if v<500:
        return
    if len(t)==N:
        res+=1
        return
    for i in range(N):
        if i not in t:
            func(t+[i],v-K+A[i])
func([],500)
print(res)