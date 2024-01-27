from collections import defaultdict
import sys
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    c,s=map(int,input().split())
    li.append((c,s,i))
li.sort(key=lambda x:x[1])
r=[0]*N
t=defaultdict(int)
i=0
tot=0
for c,s,idx in li:
    while li[i][1]<s:
        t[li[i][0]]+=li[i][1]
        tot+=li[i][1]
        i+=1
    r[idx]=tot-t[c]
for i in r:
    print(i)