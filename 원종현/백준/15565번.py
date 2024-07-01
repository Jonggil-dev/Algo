N,K=map(int,input().split())
li=list(map(int,input().split()))
st,end=0,0
r=10**9
co=0
if li[0]==1:
    co+=1
while st<len(li) and end<len(li):
    if co<K:
        end+=1
        if end<len(li) and li[end]==1:
            co+=1
    else:
        if co==K:
            r=min(r,end-st+1)
        if st<len(li) and li[st]==1:
            co-=1
        st+=1
print(-1 if r==10**9 else r)

