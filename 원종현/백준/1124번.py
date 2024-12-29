import math

def func(n):
    tmp=0
    for i in range(2,int(math.sqrt(n)+1)):
        while not n%i:
            tmp+=1
            n//=i
    if n!=1:
        tmp+=1
    return tmp

a,b=map(int,input().split())
r=[1]*(b+1)
r[1]=0
for i in range(2,b+1):
    if not r[i]:
        continue
    for j in range(i*i,b+1,i):
        r[j]=0
res=0
for i in range(a,b+1):
    if r[func(i)]:
        res+=1
print(res)