from collections import deque
d=[(1,0),(1,-1),(1,1),(-1,0),(-1,-1),(-1,1),(0,1),(0,-1),(0,0)]

N,M=map(int,input().split())
li=[]
A,B,=[0,0],[0,0]
for i in range(N):
    tmp=input()
    for j in range(M):
        if tmp[j]=='A':
            A=[i,j]
        elif tmp[j]=='B':
            B=[i,j]
    li.append(tmp)

visit=[[[[-1]*M for _ in range(N)] for _ in range(M)] for _ in range(N)] # [ax][ay][bx][by]
q=deque()
q.append((A[0],A[1],B[0],B[1],0))
visit[A[0]][A[1]][B[0]][B[1]]=0

while q:
    ax,ay,bx,by,c=q.popleft()
    for i in range(9):
        anx,any=ax+d[i][0],ay+d[i][1]
        if anx<0 or N<=anx or any<0 or M<=any or li[anx][any]=='X':
           continue
        for j in range(9):
            if i==j==8:continue
            bnx,bny=bx+d[j][0],by+d[j][1]
            if bnx<0 or N<=bnx or bny<0 or M<=bny or li[bnx][bny]=='X':
                continue
            if ([bnx,bny]==[ax,ay] and [anx,any]==[bx,by]) or [anx,any]==[bnx,bny]:
                continue
            now=visit[anx][any][bnx][bny]

            if now==-1 or now>c+1:
                visit[anx][any][bnx][bny]=c+1
                if [bnx,bny]==A and [anx,any]==B:
                    print(c+1)
                    exit()
                q.append((anx,any,bnx,bny,c+1))

print(visit[B[0]][B[1]][A[0]][A[1]])