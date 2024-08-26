from collections import deque
def solution(land):
    d=[0,0,1,-1]
    answer=0
    N,M=len(land),len(land[0])
    visit=[[0]*M for i in range(N)]
    dic={}
    cnt=0
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and land[i][j]:
                cnt+=1
                visit[i][j]=cnt
                dic[cnt]=1
                q=deque()
                q.append((i,j))
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx,ny=x+d[k],y+d[3-k]
                        if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and land[nx][ny]:
                            q.append((nx,ny))
                            visit[nx][ny]=cnt
                            dic[cnt]+=1
    res=[0]*(M)
    for j in range(M):
        tmp={}
        for i in range(N):
            if visit[i][j]!=0 and visit[i][j] not in tmp:
                tmp[visit[i][j]]=dic[visit[i][j]]
        res[j]=sum(tmp.values())
    return max(res)
