N=int(input())
P=list(map(int,input().split()))
tmp=P
tar=list(map(int,input().split()))
people=[0,1,2]*(N//3)
new=[0]*(N)
r=0

while P!=people:
    for i in range(N):
        new[tar[i]]=P[i]
    P=new
    new=[0]*(N)
    r+=1
    if tmp==P:
        r=-1
        break
print(r)