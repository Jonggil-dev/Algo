li=[[0]*10]
for i in range(9):
    tmp=input()
    li.append([0]+[i for i in tmp])
def row(x,num):
    for i in range(1,10):
        if str(num)==li[x][i]:
            return False
    return True

def col(y,num):
    for i in range(1,10):
        if str(num)==li[i][y]:
            return False
    return True

def squ(x,y,num):
    for dx in range(1,4):
        for dy in range(1,4):
            nx=((x-1)//3)*3+dx
            ny=((y-1)//3)*3+dy
            if li[nx][ny]==str(num):
                return False
    return True
def func(dep):
    if dep>=len(search_place):
        print(*[''.join(i[1:]) for i in li[1:]],sep='\n')
        exit()
    x,y=search_place[dep]
    for z in range(1,10):
        if row(x,z) and col(y,z) and squ(x,y,z):
            li[x][y]=str(z)
            func(dep+1)
            li[x][y]='0'
search_place=[]
for i in range(1,10):
    for j in range(1,10):
        if li[i][j]=='0':
            search_place.append((i,j))
func(0)