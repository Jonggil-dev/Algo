import sys
input=sys.stdin.readline

l,w,h=map(int,input().split())
tot=l*w*h
N=int(input())
li=[list(map(int,input().split())) for i in range(N)]
li.sort(reverse=True)
res=0
now=0
for i,j in li:
    now*=8
    c=2**i

    limit=min(j,(l//c)*(w//c)*(h//c)-now)
    res+=limit
    now+=limit



print(res if tot==now else -1)