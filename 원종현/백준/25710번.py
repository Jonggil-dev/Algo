from itertools import combinations_with_replacement
from collections import Counter
N=int(input())
li=Counter(map(int,input().split()))
res=0
for i,j in combinations_with_replacement(li,2):
    if i!=j or li[i]>1:
        res=max(res,sum(map(int,str(i*j))))
print(res)