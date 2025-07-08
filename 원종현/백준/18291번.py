import sys
input=sys.stdin.readline
mod=1000000007
def func(x):
    a,b=2,x
    tmp=1
    while b:
        if b%2==1:
            tmp*=a
            tmp%=mod
        a*=a
        a%=mod
        b//=2
    return tmp

for i in range(int(input())):
    now=int(input())
    if now==1:
        print(1)
    else:
        print(func(now-2))