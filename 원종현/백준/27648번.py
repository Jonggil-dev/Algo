N,M,K=map(int,input().split())

li=[]
for i in range(N):
    tmp=[]
    for j in range(M):
        tmp.append(i+j+1)
    li.append(tmp)

if li[N-1][M-1]<=K:
    print('YES')
    for i in li:
        print(" ".join(map(str,i)))
else:
    print("NO")