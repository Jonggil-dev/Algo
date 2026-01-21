import sys
input=sys.stdin.readline

N=int(input())
li=[list(map(int,input().split())) for i in range(N)]
li.sort()
tot=sum(i for _,i in li)
tmp=0
for a,b in li:
    tmp+=b
    if tmp>=(tot+1)//2:
        print(a)
        break