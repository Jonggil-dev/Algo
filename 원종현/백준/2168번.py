X,Y=map(int,input().split())

def func(a,b):
    if b>a:
        a,b=b,a
    while True:
        if b==0:
            break
        a,b=b,a%b
    return a
print(X+Y-func(X,Y))