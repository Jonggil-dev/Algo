N,M=map(int,input().split())
li=[]
ans=[0]*N
res=[]
for i in range(N):
    tmp=sorted(list(map(int,input().split())))
    li.append(tmp)
for i in range(M):
    tmp=[]
    for j in range(N):
        tmp.append(li[j][i])
    for j in range(N):
        if max(tmp)==tmp[j]:
            ans[j]+=1

for i in range(N):
    if ans[i]==max(ans):
        res.append(i+1)
print(*res)