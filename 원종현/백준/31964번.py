N=int(input())
X=list(map(int,input().split()))
T=list(map(int,input().split()))

res=2*X[N-1]
for i in range(N):
    res=max(res,T[i]+X[i])
print(res)