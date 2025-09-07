N=int(input())
res=0
for i in range(2,int(N/2+1)):
    res+=i*(N//i-1)%1000000
print(res%1000000)