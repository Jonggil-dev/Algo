N,K=map(int,input().split())
A=list(map(int,input().split()))
P=list(map(int,input().split()))
li=[]
for i in range(N):
    if A[i]<=K:
        li.append((A[i],P[i]))
li.sort(key=lambda x:(x[0],-x[1]))
res=0
def func(idx,h,v,d):
    global res
    res=max(res,v)
    for i in range(idx,len(li)):
        damages=d+li[i][0]
        if h-damages>=0:
            func(i+1,h-damages,v+li[i][1],damages)

func(0,K,0,0)
print(res)