N,A,B,C=map(int,input().split())
def func(x):
    if x<=1:
        return 1
    else:
        return x*func(x-1)
print(func(N)//(func(A)*func(B)*func(C)))