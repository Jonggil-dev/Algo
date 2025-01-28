N,M=map(int,input().split())
li=list(map(int,input().split()))
f=list(map(int,input().split()))

res=0
for i in li[:M]:
    if i not in f:
        res+=1
print(res)