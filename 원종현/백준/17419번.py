N=int(input())
K=input()
res=0
for i in range(N):
    if K[i]=='1':
        res+=1
print(res)