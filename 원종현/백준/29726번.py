N,M=map(int,input().split())
li=list(map(int,input().split()))
suf=[0]*N
suf[-1]=li[-1]
for i in range(N-2,-1,-1):
    suf[i]=max(suf[i+1],li[i])
res=-10**9
for i in range(M+1):
    res=max(res,suf[N-1-M+i]-li[i])
print(res)