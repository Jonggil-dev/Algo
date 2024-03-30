N=int(input())
res,s=0,0
st,end=0,0
while end<=N:
    if s<N:
        end+=1
        s+=end
    elif s>N:
        s-=st
        st+=1
    else:
        res+=1
        end+=1
        s+=end
print(res)