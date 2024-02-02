from collections import deque

def move(x, y, dx, dy):
    count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs(rx, ry, bx, by):
    visited = {}
    queue = deque()
    queue.append((rx, ry, bx, by, 1))
    visited[(rx, ry, bx, by)] = True

    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break

        for i in range(4):
            nrx, nry, rcount = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcount = move(bx, by, dx[i], dy[i])

            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    return depth

                if nrx == nbx and nry == nby:
                    if rcount > bcount:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited:
                    visited[(nrx, nry, nbx, nby)] = True
                    queue.append((nrx, nry, nbx, nby, depth + 1))
    return -1


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


print(bfs(rx, ry, bx, by))
