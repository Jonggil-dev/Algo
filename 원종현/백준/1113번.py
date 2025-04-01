from collections import deque
d=[0,0,1,-1]
N,M=map(int,input().split())
li=[input() for _ in range(N)]
maxh=max([max([int(j) for j in i]) for i in li])
res=0
flood=[[0]*(M) for _ in range(N)] #1이면 물새는지역



for h in range(1,maxh):
    visit=[[0]*(M) for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if (x==0 or x==N-1 or y==0 or y==M-1) and int(li[x][y])<=h:
                flood[x][y]=1
                print(f'침수! :({x},{y})')
    for x in range(N):
        for y in range(M):

            print(f'({x},{y}) 시작')
            for i in flood:
                print(i)

            print('---')

            flag=1
            flood_list=[]
            cnt=0

            if not visit[x][y] and not flood[x][y] and int(li[x][y])<=h:
                q=deque([])
                q.append((x,y))
                flood_list.append((x,y))
                visit[x][y]=1
                cnt+=1
                while q:
                    nx,ny=q.popleft()
                    chk=0
                    for i in range(4):
                        dx,dy=nx+d[i],ny+d[3-i]
                        if 0<=dx<N and 0<=dy<M:
                            if not visit[dx][dy]:
                                if not flood[dx][dy] and int(li[dx][dy])<=h:
                                    q.append((dx,dy))
                                    flood_list.append((dx,dy))
                                    visit[dx][dy]=1
                                    cnt+=1
                                elif flood[dx][dy]:
                                    print(f'({x},{y})->({nx},{ny})->({dx,dy}) 여기침수')
                                    flag=0
                if flag:
                    print(f'{h}-{res}-{cnt} : ({x},{y})에서 획득. {flood_list}')
                    res+=cnt
                else:
                    print(f'{h}-{res}-{cnt} : ({x},{y})에서 침수. {flood_list}')
                    for fx,fy in flood_list:
                        flood[fx][fy]=1
print(res)