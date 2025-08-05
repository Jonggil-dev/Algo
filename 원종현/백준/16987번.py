import sys
input=sys.stdin.readline

N=int(input())

health,weight=[],[]
for _ in range(N):
    a,b=map(int,input().split())
    health.append(a)
    weight.append(b)
res=0
health.append(1)
def func(li,idx,c):
    global res
    res=max(res,c)
    if idx>N-1:
        return

    for tar in range(N):
        if li[tar]<=0 or tar==idx:
            continue
        li[idx]-=weight[tar]
        li[tar]-=weight[idx]
        k=0
        if li[idx]<=0:k+=1
        if li[tar]<=0:k+=1
        for j in range(idx+1,N+1):
            if li[j]>0:
                func(li,j,c+k)
                break
        li[idx]+=weight[tar]
        li[tar]+=weight[idx]

func(health,0,0)
print(res)