import sys
input=sys.stdin.readline

N=int(input())
li=list(map(int,input().split()))
le=0
cnt=[0]*11
min_v,max_v=li[0],li[0]
cnt[li[0]]+=1
res=0
for ri in range(1,N):
    cnt[li[ri]]+=1
    if li[ri]<min_v:
        min_v=li[ri]
    elif li[ri]>max_v:
        max_v=li[ri]
    while max_v-min_v>2:
        cnt[li[le]]-=1
        le+=1
        while min_v<=10 and cnt[min_v]==0:
            min_v+=1
        while max_v>=1 and cnt[max_v]==0:
            max_v-=1
    res=max(res,ri-le+1)
print(res)