N=int(input())
li=[0]*(1001)
li[2]=1
for i in range(4,N+1):
    if not li[i-1]:
        li[i]=1
    if not li[i-3]:
        li[i]=1
    if not li[i-4]:
        li[i]=1

print("SK" if li[N] else "CY")