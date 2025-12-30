from itertools import combinations
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    li=[]
    for i in range(N):
        x,y=map(int,input().split())
        li.append((x,y))
    if N==2:
        print(((li[1][1]-li[0][1])**2+(li[1][0]-li[0][0])**2)**0.5)
        continue

    res=10**7
    tot=[0,0]
    for x,y in li:
        tot[0]+=x
        tot[1]+=y
    for i in combinations(li,N//2):
        a,b=0,0
        for x,y in i:
            a+=x
            b+=y
        res=min(res,((tot[0]-2*a)**2+(tot[1]-2*b)**2)**0.5)
    print(res)
