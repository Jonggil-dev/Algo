from itertools import combinations
N,L,R,X=map(int,input().split())
li=list(map(int,input().split()))
res=0
for i in range(2,N+1):
    comb=list(combinations(li,i))
    for c in  range(len(comb)):
        combi=sorted(comb[c])
        if combi[-1]-combi[0]>=X and L<=sum(combi)<=R:
            res+=1
print(res)