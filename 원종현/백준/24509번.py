import sys
input=sys.stdin.readline

N=int(input())
li=[[]]
check=[0]*(N+1)
for i in range(N):
    li.append(list(map(int,input().split())))
v=2000000
res=[]
for i in range(1,5):
    max_v=-1
    for j in range(1,N+1):
        if check[li[j][0]]==0:
            if li[j][i]>max_v:
                max_v=li[j][i]
                v=li[j][0]
            elif li[j][i]==max_v:
                v=min(v,li[j][0])
    res.append(v)
    check[v]=1
print(*res)
