N,K=map(int,input().split())
li=list(map(int,input().split()))
arr=[]
for i in range(N-1):
    tmp=li[i+1]-li[i]
    arr.append(tmp)
arr.sort()
res=0
for i in range(N-K):
    res+=arr[i]
print(res)