N=int(input())
st,end=1,N
res=[]
while st<end:
    res.append(st)
    res.append(end)
    st+=1
    end-=1
if st==end:
    res.append(st)
print(*res)