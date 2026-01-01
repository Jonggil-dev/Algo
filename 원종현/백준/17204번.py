N,K=map(int,input().split())
li=[int(input()) for _ in range(N)]
a,b=0,0
for i in range(N):
    tmp=li[a]
    b+=1
    if li[a]==K:
        print(b)
        break
    a=tmp
else:
    print(-1)