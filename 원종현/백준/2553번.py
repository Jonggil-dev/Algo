N=int(input())
res=1
for i in range(1,N+1):
    res*=i
res=str(res)
for i in range(len(res)-1,-1,-1):
    if int(res[i])!=0:
        print(res[i])
        break