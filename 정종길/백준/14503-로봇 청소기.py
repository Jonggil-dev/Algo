def check_room(i, j):
    global direction
    for _ in range(4):
        direction = ((direction - 1) % 4)
        ni, nj = i + delta[direction][0], j + delta[direction][1]
        if 0 <= ni < N and 0 <= nj < M:
            if Arr[ni][nj] == 0:
                return True
    return False

def robot(si, sj):
    global cnt, direction
    if Arr[si][sj] == 1:
        return False

    else:
        if Arr[si][sj] == 0:
            Arr[si][sj] = 2
            cnt += 1
        if check_room(si, sj):
            robot(si + delta[direction][0], sj + delta[direction][1])
        else:
            robot(si - delta[direction][0], sj - delta[direction][1])

N,M = map(int,input().split())
si, sj, direction = map(int,input().split())
Arr = [list(map(int,input().split())) for _ in range(N)]
delta = [(-1,0),(0,1),(1,0),(0,-1)]
cnt = 0
robot(si,sj)
print(cnt)