A,B=map(int,input().split())
def gcd(x,y):
    mod=x%y
    while mod>0:
        x,y=y,mod
        mod=x%y
    return y

print('1'*gcd(A,B))