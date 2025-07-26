import math

def func(x):
    tmp={}
    while True:
        n=str(x)
        x=0
        for i in range(len(n)):
            x+=int(n[i])**2
        if x==1:
            return 1
        if x in tmp:
            return 0
        else:
            tmp[x]=1

so=set()
chk=[1]*(1000001)
for i in range(2,int(1000001**0.5)+1):
    if chk[i]:
        for j in range(i*i,1000001,i):
            chk[j]=0
for i in range(2,1000001):
    if chk[i]:
        so.add(i)


N=int(input())
for i in range(7,N+1):
    if i in so:
        if func(i):
            print(i)