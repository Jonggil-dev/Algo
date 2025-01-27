import sys
input=sys.stdin.readline

N=int(input())
li=[int(input()) for _ in range(N)]
tmp=[0]*(max(li)+1)
res=[0]*(N)
for i in li:
    tmp[i]+=1
for i in range(N):
    k=1
    while k*k<=li[i]:
        if li[i]%k==0:
            if k*k!=li[i]:
                res[i]+=tmp[k]+tmp[li[i]//k]
            else:
                res[i]+=tmp[k]
        k+=1
r=''
for i in res:
    r+=str(i-1)+'\n'
print(r)