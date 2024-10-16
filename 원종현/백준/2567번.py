N=int(input())
li=[[0]*(101) for _ in range(101)]
d=[0,0,1,-1]
for  _ in range(N):
    x,y=map(int,input().split())
    for dx in range(x,x+10):
        for dy in range(y,y+10):
            li[dx][dy]=1

res=0
for i in range(1,101):
    for j in range(1,101):
        if li[i][j]:
            tmp=0
            for k in range(4):
                if li[i+d[k]][j+d[3-k]]:
                    tmp+=1
            if tmp==3:
                res+=1
            elif tmp==2:
                res+=2
print(res)