import sys
input=sys.stdin.readline

N,M=map(int,input().split())
X,Y=[],[]
for i in range(M):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
res=0
for i in range(M):
    res+=abs(X[i]-X[M//2])+abs(Y[i]-Y[M//2])
print(res)