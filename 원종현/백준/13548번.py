from collections import defaultdict
import sys
input=sys.stdin.readline

N=int(input())
sq=N**0.5
li=list(map(int,input().split()))
M=int(input())
query=[]
for idx in range(M):
    i,j=map(lambda x:int(x)-1,input().split())
    query.append((i//sq,i,j,idx))
query.sort(key=lambda x:(x[0],x[2]))

le,ri=0,-1
dk=defaultdict(int)
dv=defaultdict(set)
#for i in li:
#    dk[i]+=1
cnt=0
#for k,v in dk.items():
#    dv[v].add(k)
#    cnt=max(v,cnt)
res=[0]*M
for _,next_le,next_ri,idx in query:
    while le<next_le:
        dv[dk[li[le]]].discard(li[le])
        if dk[li[le]]==cnt and not dv[dk[li[le]]]:
            cnt-=1
        dv[dk[li[le]]-1].add(li[le])
        dk[li[le]]-=1
        le+=1

    while next_le<le:
        le-=1
        dv[dk[li[le]]].remove(li[le])
        dv[dk[li[le]]+1].add(li[le])
        cnt=max(dk[li[le]]+1,cnt)
        dk[li[le]]+=1

    while ri<next_ri:
        ri+=1
        dv[dk[li[ri]]].discard(li[ri])
        dv[dk[li[ri]]+1].add(li[ri])
        cnt=max(dk[li[ri]]+1,cnt)
        dk[li[ri]]+=1
    while next_ri<ri:
        dv[dk[li[ri]]].remove(li[ri])
        if dk[li[ri]]==cnt and not dv[dk[li[ri]]]:
            cnt-=1
        dv[dk[li[ri]]-1].add(li[ri])
        dk[li[ri]]-=1
        ri-=1
    res[idx]=cnt

print(*res,sep="\n")