import sys
input=sys.stdin.readline
N=int(input())
li=[int(input()) for _ in range(N)]
li.sort(reverse=True)
res=0
for i in range(N):
    if li[i]-i<0:
        continue
    res+=li[i]-i
print(res)
