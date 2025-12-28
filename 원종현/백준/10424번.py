N=int(input())
li=list(map(int,input().split()))
res={}
for i in range(N):
    res[li[i]]=i+1
for i in range(N):
    print(i+1-res[i+1])