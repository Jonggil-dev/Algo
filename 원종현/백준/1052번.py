N,K=map(int,input().split())
res=0
while bin(N).count('1')>K:
    N+=1
    res+=1
print(res)