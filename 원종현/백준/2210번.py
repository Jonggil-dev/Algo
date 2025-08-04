d=[0,0,1,-1]
li=[input().split() for _ in range(5)]
res=set()
tmp=set()
def func(now,x,y):
    if len(now)==6:
        res.add(now)
        return

    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<5 and 0<=ny<5:
            func(now+li[nx][ny],nx,ny)

for x in range(5):
    for y in range(5):
        func('',x,y)
print(len(res))