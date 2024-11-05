N,K=map(int,input().split())
li=sorted(list(map(int,input().split())))
res=0
for i in range(1,K+1):
    res+=li[-i]-i+1
print(res)
