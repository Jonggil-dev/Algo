N,Z,M=map(int,input().split())
li=set(map(int,input().split()))
f=0
if Z==N:Z=0

for i in range(1,N):
    tmp=[(1+i*j)%N for j in range(N)]
    for j in tmp:
        if j in li:
            break
        if j==Z:
            print(i)
            f=1
            break
    if f:
        break