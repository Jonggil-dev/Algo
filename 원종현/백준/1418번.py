N=int(input())
K=int(input())
p=[1]*(N+1)
for i in range(2,int(N**0.5)+1):
    if p[i] :
        for j in range(2*i,N+1,i):
            p[j]=0
li=[1]*(N+1)
for i in range(2,N+1):
    if p[i] and i>K:
        for j in range(i,N+1,i):
            li[j]=0
print(sum(li)-1)