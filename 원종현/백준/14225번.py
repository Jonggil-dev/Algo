from itertools import combinations
N=int(input())
li=list(map(int,input().split()))
tmp=set()
for i in range(1,N+1):
    for j in list(combinations(li,i)):
        tmp.add(sum(j))
tmp=set([i for i in range(1,max(tmp)+2)])-tmp
print(min(tmp))