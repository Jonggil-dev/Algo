N,a,b=map(int,input().split())
res=[]
for i in range(1,a):
    res.append(i)
res.append(max(a,b))
for i in range(b-1,0,-1):
    res.append(i)
if len(res)>N:
    print(-1)
    exit()

print(res[0],end=" ")
for i in range(N-len(res)):
    print(1,end=" ")
for i in range(1,len(res)):
    print(res[i],end=" ")