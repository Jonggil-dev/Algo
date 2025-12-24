N,K=map(int,input().split())
li=list(map(int,input().split()))
res=[0]*N
res[0]=li[0]
for i in range(1,N):
    res[i]=res[i-1]+li[i]
res.sort(reverse=True)
print(sum(res[:K]))