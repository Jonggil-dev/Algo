N=int(input())
li=list(map(int,input().split()))
check=set(li)
d={}
st=0
for i in li:
    if not i%3 and i//3 in check:
        d[i//3]=i
        continue
    if i*2 in check:
        d[i*2]=i
        continue
    st=i

res=[]
while True:
    res.append(st)
    if st not in d:
        break
    st=d[st]
print(*res[::-1])