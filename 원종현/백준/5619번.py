from itertools import permutations

N=int(input())
li=sorted([int(input()) for _ in range(N)])
res=sorted([int(str(x)+str(y)) for x,y in permutations(li[:4],2)])
print(res[2])
