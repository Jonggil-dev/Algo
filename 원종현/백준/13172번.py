S=1000000007
def ans(n,s):
    return s*func(n,S-2)%S
def func(b,t):
    if t==1:
        return b%S
    if t%2==0:
        tmp=func(b,t//2)
        return (tmp*tmp)%S
    else:
        return b*func(b,t-1)%S
res=0
m=int(input())
for _ in range(m):
    n,s=map(int,input().split())
    res+=ans(n,s)
    res%=S
print(res)