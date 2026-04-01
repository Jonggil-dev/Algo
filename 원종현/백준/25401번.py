N=int(input())
li=list(map(int,input().split()))
s=set()
for i in range(N-1):
    for j in range(i+1,N):
        now=(li[j]-li[i])/(j-i)
        if not now-int(now):
            s.add((now,li[j]-now*j))

res=[]
for a,b in s:
    tmp=0
    for i in range(N):
        if li[i]!=a*i+b:
            tmp+=1
    res.append(tmp)
print(min(res))