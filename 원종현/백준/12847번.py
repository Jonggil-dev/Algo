import sys
input=sys.stdin.readline
M=int(input())
tot=0
xor=0
for i in range(M):
    li=list(map(int,input().split()))
    if li[0]==1:
        tot+=li[1]
        xor=xor^li[1]
    elif li[0]==2:
        tot-=li[1]
        xor=xor^li[1]
    elif li[0]==3:
        print(tot)
    elif li[0]==4:
        print(xor)