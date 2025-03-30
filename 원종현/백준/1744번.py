N=int(input())
tmp=[int(input()) for _ in range(N)]
p,m=sorted([i for i in tmp if i>1],reverse=True),sorted([i for i in tmp if i<=0])
res=tmp.count(1)
print(p)
print(m)
for i in range(0,len(p)-1,2):
    res+=p[i]*p[i+1]
for i in range(0,len(m)-1,2):
    res+=m[i]*m[i+1]
if len(p)%2:
    res+=p[-1]
if len(m)%2:
    res+=m[-1]
print(res)
