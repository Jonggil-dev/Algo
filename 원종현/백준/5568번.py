from itertools import permutations
N=int(input())
K=int(input())
li=[input() for _ in range(N)]
tmp=set(''.join(i) for i in permutations(li,K))
print(len(tmp))