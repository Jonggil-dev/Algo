from collections import deque

def solution(maze):
    answer = 10**9
    N,M=len(maze),len(maze[0])
    red,blue,red_end,blue_end=[0,0],[0,0],[0,0],[0,0]
    d=[0,0,1,-1]
    for i in range(N):
        for j in range(M):
            if maze[i][j]==1:
                red=[i,j]
            elif maze[i][j]==2:
                blue=[i,j]
            elif maze[i][j]==3:
                red_end=[i,j]
            elif maze[i][j]==4:
                blue_end=[i,j]

    q=deque()
    q.append((red,blue,0,{(red[0],red[1])},{(blue[0],blue[1])}))
    while q:
        r,b,turn,rv,bv=q.popleft()
        for i in range(4):
            flag1=0
            if r==red_end:
                flag1=1
            nrx,nry=[r[0]+d[i],r[1]+d[3-i]] if r!=red_end else r
            if ((nrx,nry) not in rv or [nrx,nry]==red_end) and 0<=nrx<N and 0<=nry<M and maze[nrx][nry]!=5:
                for j in range(4):
                    flag2=0
                    if b==blue_end:
                        flag2=1
                    nbx,nby=[b[0]+d[j],b[1]+d[3-j]] if b!=blue_end else b
                    if ((nbx,nby) not in bv or [nbx,nby]==blue_end) and 0<=nbx<N and 0<=nby<M and maze[nbx][nby]!=5:
                        if (r==[nbx,nby] and b==[nrx,nry]) or [nrx,nry]==[nbx,nby]:
                            continue
                        if flag1 and flag2:
                            answer=min(answer,turn)
                            break
                        q.append(([nrx,nry],[nbx,nby],turn+1,rv|{(nrx,nry)},bv|{(nbx,nby)}))
                    if flag2:
                        break
            if flag1:
                break
    if answer==10**9:
        answer=0
    return answer
