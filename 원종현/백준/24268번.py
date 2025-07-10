from itertools import permutations

N,D=map(int,input().split())
for i in range(1,D):
    for j in permutations(list(set([i for i in range(D)])-set([i])),D-1):
        now=int(str(i)+''.join(map(str,j)),D)
        if now>N:
            print(now)
            exit()
print(-1)