N,K=map(int,input().split())
S=input()
res=0
if K==1:
    res=S
elif (N-K)%2:
    res=S[K-1:]+S[:K-1]
else:
    res=S[K-1:]+S[K-2::-1]
print(res)