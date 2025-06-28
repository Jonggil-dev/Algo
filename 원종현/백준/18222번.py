K=int(input())

def func(x):
    if x==0:return 0
    elif x==1:return 1
    elif x%2==0:return func(x//2)
    else:return 1-func(x//2)
print(func(K-1))