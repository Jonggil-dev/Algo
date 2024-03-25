N=int(input())
li=list(map(int,input().split()))
r=[0]*(N)
for i in range(1,N+1):
    now=li[i-1]
    count=0
    for j in range(N):
        if count==now and r[j]==0:
            r[j]=i
            break
        elif r[j]==0:
            count+=1
print(*r)