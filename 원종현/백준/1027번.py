N=int(input())
li=list(map(int,input().split()))
res=[0]*N
def func(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

for i in range(N):
    t=-float('inf')
    for j in range(i+1,N):
        s=func(j,li[j],i,li[i])
        if s<=t:
            continue
        t=max(t,s)
        res[i]+=1
        res[j]+=1
print(max(res))