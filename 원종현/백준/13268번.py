N=int(input())
res=0

while N>0:
    res=0
    for i in range(1,5):
        for j in range(i):
            N-=5
            if N<=0:
                res+=5+N
                break
            res+=5
        if N<=0:
            break

        for j in range(i):
            N-=5
            if N<=0:
                res-=5+N
                break
            res-=5
        if N<=0:
            break
print(res//5+1 if res%5 else res//5)