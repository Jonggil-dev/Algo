N,K=map(int,input().split())
li=list(map(int,input().split()))
le,ri=0,0

count=[0]*(max(li)+1)
res=0
while ri<N:
    if count[li[ri]]<K:
        count[li[ri]]+=1
        ri+=1
    else:
        count[li[le]]-=1
        le+=1
    res=max(res,ri-le)
print(res)