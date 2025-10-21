N=int(input())
li=list(map(int,input().split()))
res=[1]
for i in range(N-1,0,-1):
    if N>i+li[i-1]:
        res.append(res[N-i-li[i-1]-1]+1)
    else:
        res.append(1)
for i in res[::-1]:
    print(i,end=" ")