li=[list(map(int,input().split())) for _ in range(19)]
d=[(0,1),(1,0),(1,1),(1,-1)]

def func(x,y,i):
    tmp=[(x,y)]
    nx,ny=x+d[i][0],y+d[i][1]
    while 0<=nx<19 and 0<=ny<19 and li[x][y]==li[nx][ny]:
        tmp.append((nx,ny))
        nx,ny=nx+d[i][0],ny+d[i][1]
    return tmp

def check(x,y):
    for i in range(4):
        tmp=func(x,y,i)
        if len(tmp)==5 and ((0<=x-d[i][0]<19 and 0<=y-d[i][1]<19 and li[x][y]!=li[x-d[i][0]][y-d[i][1]]) or (not 0<=x-d[i][0]<19 or not 0<=y-d[i][1]<19)):
            return tmp
    return []

for x in range(19):
    for y in range(19):
        if li[x][y]:
            r=check(x,y)
            if len(r)==5:
                print(li[x][y])
                nx,ny=sorted(r,key=lambda x:(x[1],x[0]))[0]
                print(nx+1,ny+1)
                exit()
print(0)