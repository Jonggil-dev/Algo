d=[0,0,1,-1]
R,C,K=map(int,input().split())
li=[list(input()) for i in range(R)]
res=0
def func(x,y,c):
    global res
    if c==K and x==0 and y==C-1:
        res+=1
    for i in range(4):
        nx=x+d[i]
        ny=y+d[3-i]
        if 0<=nx<R and 0<=ny<C and li[nx][ny]=='.':
            li[nx][ny]='T'
            func(nx,ny,c+1)
            li[nx][ny]='.'
li[R-1][0]='T'
func(R-1,0,1)
print(res)