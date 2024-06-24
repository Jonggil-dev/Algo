N,M=list(map(int,input().split()))
li=[[-1]*(M+1) for _ in range(N+1)]

def func(x,y):
    if x==1 or x==y or y==0:
        return 1

    else:
        if li[x][y]==-1:
            li[x][y]=func(x-1,y)+func(x-1,y-1)
        return li[x][y]
print(func(N,M))