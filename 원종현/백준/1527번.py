import sys
from itertools import product
input=sys.stdin.readline
a,b=map(int,input().split())
x=len(str(a))
y=len(str(b))

res=0
for i in range(x,y+1):
    li=list(product([4,7],repeat=i))
    for j in li:
        t=int(''.join(map(str,j)))
        if a<=t<=b:
            res+=1
print(res)