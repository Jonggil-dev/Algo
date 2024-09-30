N,K=map(int,input().split())

tmp=K*(K+1)//2
if N<tmp:
    print(-1)
elif (N-tmp)%K==0:
    print(K-1)
else:
    print(K)