from collections import defaultdict
import sys
input=sys.stdin.readline

N=int(input())
sq=N**0.5
li=list(map(int,input().split()))
M=int(input())
query=[]
for idx in range(M):
    i,j=map(int,input().split())
    i-=1
    j-=1
    query.append((i//sq,i,j,idx))
query.sort(key=lambda x:(x[0],x[2]))
le,ri=0,N-1
d=defaultdict(int)
for i in li:
    d[i]+=1
res=[0]*M
cnt=len(d)
for _,next_le,next_ri,idx in query:
    while le<next_le:
        d[li[le]]-=1
        if not d[li[le]]:
            cnt-=1
        le+=1
    while next_le<le:
        le-=1
        if not d[li[le]]:
            cnt+=1
        d[li[le]]+=1
    while ri<next_ri:
        ri+=1
        if not d[li[ri]]:
            cnt+=1
        d[li[ri]]+=1
    while next_ri<ri:
        d[li[ri]]-=1
        if not d[li[ri]]:
            cnt-=1
        ri-=1
    res[idx]=cnt

print(*res,sep="\n")