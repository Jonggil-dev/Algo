N=int(input())
li=[list(map(int,input().split())) for i in range(N)]
if N==2:
    print(1,1)
else:
    res=[(li[0][1]+li[0][2]-li[1][2])//2]
    for i in range(1,N):
        res.append(li[0][i]-res[0])
    print(*res)