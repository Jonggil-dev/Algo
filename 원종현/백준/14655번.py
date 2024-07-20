N=int(input())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
M,N=0,0
for i in X:
    N+=abs(i)
for i in Y:
    M+=abs(i)
print(N+M)