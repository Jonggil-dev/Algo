def func(l,r,k):
    if l>r or k==0:
        return 0
    if dp[l][r][k]!=-1:
        return dp[l][r][k]
    tmp=(0,-1,-1)
    t=func(l+1,r,k)
    t2=func(l+1,r,k-1)+li[l]
    if t2>t:
        t=t2
        tmp=(1,l,l)

    for i in range(l+1,r+1):
        for j in range(k):
            t3=func(l+1,i-1,k-j-1)+func(i+1,r,j)+li[l]*li[i]
            if t3>t:
                t=t3
                tmp=(2,i,j)
    dp[l][r][k]=t
    check[l][r][k]=tmp
    return dp[l][r][k]

def trace(l,r,k):
    if l>r or k==0:
        return
    now=check[l][r][k]
    if now==0:
        return
    t,i,j=now
    if t==0:
        trace(l+1,r,k)
    elif t==1:
        res1.append(l+1)
        res2[l]=l+1
        trace(l+1,r,k-1)
    else:
        res1.append(l+1)
        res2[l]=i+1
        res2[i]=l+1
        trace(l+1,i-1,k-j-1)
        trace(i+1,r,j)

N,K=map(int,input().split())
li=list(map(int,input().split()))
dp=[[[-1]*(K+1) for _ in range(N)] for _ in range(N)]
check=[[[0]*(K+1) for _ in range(N)] for _ in range(N)]
func(0,N-1,K)
res1=[]
res2=[0]*N
trace(0,N-1,K)

res1+=[0]*(K-len(res1))
print(*res1,sep='\n')
print(*res2,sep='\n')