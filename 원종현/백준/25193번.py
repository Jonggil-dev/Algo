import math
N=int(input())
S=input()
r1,r2=0,0
for i in S:
    if i=='C':
        r1+=1
    else:
        r2+=1
print(math.ceil(r1/(r2+1)))