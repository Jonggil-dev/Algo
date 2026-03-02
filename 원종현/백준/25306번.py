A,B=map(int,input().split())

def func(x):
    st=x//4*4
    tmp=0
    for i in range(st,x+1):
        tmp^=i
    return tmp
print(func(A-1)^func(B))