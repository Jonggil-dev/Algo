import sys
input=sys.stdin.readline

def miller(n,a):
    if a%n==0:
        return 1
    d=n-1
    while d%2==0:
        if pow(a,d,n)==n-1:
            return 1
        d//=2
    tmp=pow(a,d,n)
    return tmp==n-1 or tmp==1

def prime(n):
    if n<=1:
        return 0
    if n<=3:
        return 1
    if n%2==0:
        return 0
    bases=[2,3,5,7,11,13,17,19,23,29,31,37]
    for i in bases:
        if n==i:
            return 1
        if not miller(n,i):
            return 0
    return 1
res=0
for i in range(int(input())):
    A=int(input())
    if prime(2*A+1):
        res+=1
print(res)
