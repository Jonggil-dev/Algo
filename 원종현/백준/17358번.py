N=int(input())
res=1
for i in range(N-1,1,-2):
    res*=i
print(res%(1000000007))