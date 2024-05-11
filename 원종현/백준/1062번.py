import sys
from itertools import combinations
input=sys.stdin.readline

def tobit(word):
    b=0
    for c in word:
        b=b|(1 <<ord(c)-ord('a'))
    return b

N,K=map(int,input().split())
words=[input().rstrip() for _ in range(N)]
bits=list(map(tobit,words))
base=tobit('antic')

if K<5:
    print(0)
else:
    alp=[1<<i for i in range(26) if not (base&1<<i)]
    ans=0
    for combination in combinations(alp,K-5):
        k_b=sum(combination)|base
        count=0
        for b in bits:
            if b&k_b==b:
                count+=1
        ans=max(ans,count)
    print(ans)