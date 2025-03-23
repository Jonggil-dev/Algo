import sys
input=sys.stdin.readline
N=int(input())
li=[int(input()) for _ in range(N)]
li.sort()
res=0
for i in range(1,N+1):
    res+=abs(i-li[i-1])
print(res)