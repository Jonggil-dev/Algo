import sys
input=sys.stdin.readline

N=int(input())
li=sorted([int(input()) for _ in range(N)])
set1=set()
res=0
for x in range(N):
    for y in range(x,N):
        set1.add(li[x]+li[y])

for k in range(N-1,-1,-1):
    for z in range(N-1,-1,-1):
        if li[k]-li[z] in set1:
            res=max(res,li[k])
print(res)

