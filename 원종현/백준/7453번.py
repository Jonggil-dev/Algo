import sys
from collections import defaultdict
input=sys.stdin.readline


N=int(input())
li=[]
A,B,C,D=[],[],[],[]
for i in range(N):
    tmp=list(map(int,input().split()))
    A.append(tmp[0])
    B.append(tmp[1])
    C.append(tmp[2])
    D.append(tmp[3])

dic=defaultdict(int)
for i in A:
    for j in B:
        dic[i+j]+=1

res=0
for i in C:
    for j in D:
        if -(i+j) in dic:
            res+=dic[-(i+j)]
print(res)