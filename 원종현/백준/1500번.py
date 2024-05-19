S,K=map(int,input().split())
r=S//K
tmp=S%K
res=1
for _ in range(K):
    if tmp>0:
        res*=(r+1)
        tmp-=1
    else:
        res*=r
print(res)