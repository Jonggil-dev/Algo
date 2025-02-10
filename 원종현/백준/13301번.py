N=int(input())
li=[0]*(81)
li[0]=4
li[1]=6
for i in range(2,N+1):
    li[i]=li[i-1]+li[i-2]
print(li[N-1])