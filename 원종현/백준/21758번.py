N=int(input())
li=list(map(int,input().split()))
res=0
tmp=[li[0]]
for i in range(1,N):
    tmp.append(tmp[i-1]+li[i])

for i in range(1,N-1):
    res=max(res,tmp[N-2]+tmp[i-1]-li[i],tmp[N-1]-li[0]-li[i]+tmp[N-1]-tmp[i],tmp[N-2]-li[0]+li[i])
print(res)