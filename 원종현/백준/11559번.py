li=[list(input()) for _ in range(12)]
d=[0,0,1,-1]
def get_height(height):
    for y in range(6):
        for x in range(11,-1,-1):
            if li[x][y]=='.':
                break
            height[y]=x
    return height

def drop():
    global li
    height=get_height([0]*6)
    check=[0]*6
    for y in range(6):
        for x in range(11,-1,-1):
            if li[x][y]=='.':
                check[y]=1
            elif li[x][y]!='.' and check[y]:
                li[height[y]-1][y]=li[x][y]
                li[x][y]='.'
                height[y]-=1

def boom(x,y,c,visit):
    global li
    v,l=0,[]
    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<12 and 0<=ny<6 and li[nx][ny]==c and not visit[nx][ny]:
            visit[nx][ny]=1
            v+=1
            l.append((nx,ny))
            nv,nl=boom(nx,ny,c,visit)
            v+=nv
            l.extend(nl)
    return v,l

def func(val):
    drop()
    diff=0
    visit=[[0]*6 for _ in range(12)]
    for x in range(12):
        for y in range(6):
            if li[x][y]!='.' and not visit[x][y]:
                visit[x][y]=1
                v,l=boom(x,y,li[x][y],visit)
                if v>=3:
                    for dx,dy in l+[[x,y]]:
                        li[dx][dy]='.'
                    diff+=1

    if not diff:
        return val
    else:
        return func(val+1)

print(func(0))