import math

K=int(input())
li=[]
for i in range(2,math.ceil(math.sqrt(K))+1):
    while K%i==0:
        li.append(i)
        K//=i

if K!=1:
    li.append(K)
print(len(li))
print(*li)