def func(x):
    for i in range(2,int(x**0.5)):
        if x%i==0:
            return 0
    return 1

def func2(a,p):
    mod=p
    tmp=1
    while p:
        if p&1==1:
            tmp*=a
            tmp%=mod
        p>>=1
        a**=2
        a%=mod
    tmp%=mod
    return tmp

while True:
    p,a=map(int,input().split())
    if p==0 and a==0:
        break
    if not func(p) and func2(a,p)==a:
        print('yes')
    else:
        print('no')