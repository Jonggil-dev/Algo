N,M=map(int,input().split())
li=[[0]*(101) for _ in range(101)]
for i in range(N):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            li[x][y]+=1
r=0
for x in range(1,101):
    for y in range(1,101):
        if li[x][y]>M:
            r+=1
print(r)