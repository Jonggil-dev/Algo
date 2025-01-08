import sys
input=sys.stdin.readline

N=int(input())

li=[0]*21
li[0]=1
for i in range(1,N+1):
    li[i]=li[i-1]*i
check=[0]*21
res=[0]*21

tmp=list(map(int,input().split()))
if tmp[0]==1:
    k=tmp[1]
    for i in range(1,N+1):
        cnt=1
        for j in range(1,N+1):
            if check[j]:
                continue
            if k<=cnt*li[N-i]:
                k-=(cnt-1)*li[N-i]
                res[i]=j
                check[j]=1
                break
            cnt+=1
    for i in range(1,N+1):
        print(res[i],end=" ")
else:
    k=1
    for i in range(1,N+1):
        cnt=0
        for j in range(1,tmp[i]):
            if not check[j]:
                cnt+=1
        k+=cnt*li[N-i]
        check[tmp[i]]=1
    print(k)