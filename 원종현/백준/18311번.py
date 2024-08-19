N,K=map(int,input().split())
li=list(map(int,input().split()))
s=[[i+1,li[i]] for i in range(N)]+[[i+1,li[i]] for i in range(N-1,-1,-1)]

for now,l in s:
    K-=l
    if K<0:
        print(now)
        break

