N=int(input())
li=[[0]*(N) for _ in range(N)]
for  i in range(N-1):
    now=int(input())
    node=map(int,input().split())
    for j in node:
        li[i][j-1]=1

for i in range(N):
    for j in range(N):
        for k in range(N):
            if li[j][i] and li[i][k]:
                li[j][k]=1

for i in range(N):
    if li[i][i]==1 and li[0][i]:
        print('CYCLE')
        break
else:
    print("NO CYCLE")