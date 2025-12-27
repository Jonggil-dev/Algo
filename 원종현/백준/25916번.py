N,M=map(int,input().split())
li=list(map(int,input().split()))
st,end=0,1
v=sum(li[st:end])
res=0
while True:
    try:
        if v<=M:
            res=max(res,v)
            v+=li[end]
            end+=1
        else:
            v-=li[st]
            st+=1
    except:
        break
print(res)