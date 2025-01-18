import sys
input=sys.stdin.readline

U,N=map(int,input().split())
p=[[]for i in range(10001)]
li=[0]*(10001)
M=10001
for i in range(N):
    name,price=input().split()
    price=int(price)
    p[price].append(name)
    li[price]+=1
for i in range(10001):
    if li[i]!=0:
        M=min(li[i],M)
for i in range(10001):
    if M==li[i]:
        print(p[i][0],i)
        break