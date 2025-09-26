import sys
input=sys.stdin.readline
N=int(input())
li=[int(input()) for _ in range(N)]
li.sort(reverse=True)
min_v=li[0]+1
res=1
for i in range(1,N):
    if min_v>li[i]+N:
        break
    min_v=max(min_v,li[i]+i+1)
    res+=1
print(res)
