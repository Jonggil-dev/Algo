A=int(input())
X=int(input())

res=1
now=A
while X:
    if X&1:
        res=(res*now)%1000000007
    now=(now**2)%1000000007
    X//=2
print(res)