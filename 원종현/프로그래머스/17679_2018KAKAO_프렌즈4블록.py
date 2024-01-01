d=[(1,0),(0,1),(1,1)]
def solution(m, n, board):
    def delete(x,y):
        tmp_delete_list=[]
        co=0
        if b[x][y]!=0:
            for idx in range(3):
                nx=x+d[idx][0]
                ny=y+d[idx][1]
                if 0<=nx<m and 0<=ny<n and b[nx][ny]==b[x][y]:
                    co+=1
        if co==3:
            tmp_delete_list=[(x,y)]
            for idx in range(3):
                nx=x+d[idx][0]
                ny=y+d[idx][1]
                tmp_delete_list.append((nx,ny))
        return tmp_delete_list


    b=[]
    for i in range(m):
        b.append(list(board[i]))
    answer = 0
    while True:
        check=0
        delete_list=[]
        for x in range(m):
            for y in range(n):
                delete_list.extend(delete(x,y))
        delete_list=set(delete_list)
        for x,y in delete_list:
            b[x][y]=0
            answer+=1
            check=1
        while True:
            cc=0
            for y in range(n-1,-1,-1):
                for x in range(m-1,0,-1):
                    if b[x][y]==0 and b[x-1][y]!=0:
                        b[x][y]=b[x-1][y]
                        b[x-1][y]=0
                        cc=1
            if not cc:
                break

        if not check:
            break
    return answer