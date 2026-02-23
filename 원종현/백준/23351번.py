N,K,A,B,=map(int,input().split())
li=[K for i in range(N)]
check=1
res=0
while check:
    for i in range(A):
        li[i]+=B
    for i in range(N):
        li[i]-=1
    li.sort()
    res+=1
    if li[0]==0:
        break

print(res)