N,X=map(int,input().split())

b,p=[1]*51,[1]*51

for i in range(1,N+1):
    b[i]=3+b[i-1]*2
    p[i]=1+p[i-1]*2
print(b)
print(p)

def func(n,x):
    if n==0:return x
    if x==1:
        return 0
    elif x<=1+b[n-1]:
        return func(n-1,x-1)
    elif x==1+b[n-1]+1:
        return p[n-1]+1
    elif x<=2+b[n-1]*2:
        return p[n-1]+1+func(n-1,(x-(b[n-1]+2)))
    else:
        return p[n]
print(func(N,X))