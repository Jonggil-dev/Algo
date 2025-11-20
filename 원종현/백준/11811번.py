N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]
a=[0]*N
check=[0]*N

for x in range(N):
    for y in range(N):
        if x==y:
            continue
        a[x]|=li[x][y]
print(*a)