a,b=map(int,input().split())
R=1000000000
fib={1:1,2:1,3:2,4:3,5:5}
def func(n):
    if n in fib:
        return fib[n]
    if n%2:
        fib[n]=(func(n//2)**2+func(n//2+1)**2)%R
    else:
        fib[n]=(func(n+1)-func(n-1))%R
    return fib[n]

print((func(b+2)-func(a+1))%R)