N=int(input())
res=N
for i in range(2,int(N**0.5)+1):
    if not N%i:
        while not N%i:
            N//=i
        res-=res/i
if N>1:
    res-=res/N
print(int(res))