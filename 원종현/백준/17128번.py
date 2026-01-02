N,Q=map(int,input().split())
A=list(map(int,input().split()))
li=list(map(int,input().split()))
tmp=[0]*N
for i in range(N):
    tmp[i]=A[i%N]*A[(i+1)%N]*A[(i+2)%N]*A[(i+3)%N]
res=sum(tmp)
for i in li:
    for j in range(4):
        tmp[i-j-1]=-tmp[i-j-1]
        res+=2*tmp[i-j-1]
    print(res)