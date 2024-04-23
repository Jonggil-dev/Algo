N,M=map(int,input().split())
li=list(map(int,input().split()))

s=li[0]
l,r=0,1
res=0
while True:
    if s<M:
        if r<N:
            s+=li[r]
            r+=1
        else:
            break
        continue
    elif s==M:
        res+=1
    s-=li[l]
    l+=1
print(res)