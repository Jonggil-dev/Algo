from itertools import permutations
N=int(input())
li=list(map(int,input().split()))

res=-10**9
for i in permutations(li):
    tmp=0
    for j in range(N-1):
        tmp+=abs(i[j]-i[j+1])
    res=max(res,tmp)
print(res)