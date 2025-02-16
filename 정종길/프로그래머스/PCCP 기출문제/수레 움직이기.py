def solution(maze):
    global answer, row, col, visited_r, visited_b
    answer = 1e9
    row = len(maze)
    col = len(maze[0])
    visited_r = [[0] * col for _ in range(row)]
    visited_b = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if maze[i][j] == 1:
                ri, rj = i, j

            if maze[i][j] == 2:
                bi, bj = i, j

    visited_r[ri][rj] = 1
    visited_b[bi][bj] = 1
    dfs(ri, rj, bi, bj, 0, maze)

    if answer == 1e9:
        answer = 0

    return answer


def dfs(ri, rj, bi, bj, cnt, arr):
    global answer, row, col, visited_r, visited_b

    if arr[ri][rj] == 3 and arr[bi][bj] == 4:
        answer = min(answer, cnt)
        return

    if arr[ri][rj] == 3:
        for dbi, dbj in (0, 1), (1, 0), (0, -1), (-1, 0):
            nbi, nbj = bi + dbi, bj + dbj
            if 0 <= nbi < row and 0 <= nbj < col:
                if not visited_b[nbi][nbj] and arr[nbi][nbj] != 5:
                    if ri == nbi and rj == nbj:
                        continue

                    visited_b[nbi][nbj] = 1
                    dfs(ri, rj, nbi, nbj, cnt + 1, arr)
                    visited_b[nbi][nbj] = 0

    elif arr[bi][bj] == 4:
        for dri, drj in (0, 1), (1, 0), (0, -1), (-1, 0):
            nri, nrj = ri + dri, rj + drj
            if 0 <= nri < row and 0 <= nrj < col:
                if not visited_r[nri][nrj] and arr[nri][nrj] != 5:
                    if nri == bi and nrj == bj:
                        continue

                    visited_r[nri][nrj] = 1
                    dfs(nri, nrj, bi, bj, cnt + 1, arr)
                    visited_r[nri][nrj] = 0

    else:
        for dri, drj in (0, 1), (1, 0), (0, -1), (-1, 0):
            nri, nrj = ri + dri, rj + drj
            if 0 <= nri < row and 0 <= nrj < col:
                if not visited_r[nri][nrj] and arr[nri][nrj] != 5:
                    for dbi, dbj in (0, 1), (1, 0), (0, -1), (-1, 0):
                        nbi, nbj = bi + dbi, bj + dbj
                        if 0 <= nbi < row and 0 <= nbj < col:
                            if not visited_b[nbi][nbj] and arr[nbi][nbj] != 5:
                                if nri == nbi and nrj == nbj:
                                    continue

                                if ri == nbi and rj == nbj and bi == nri and bj == nrj:
                                    continue

                                visited_r[nri][nrj] = 1
                                visited_b[nbi][nbj] = 1
                                dfs(nri, nrj, nbi, nbj, cnt + 1, arr)
                                visited_r[nri][nrj] = 0
                                visited_b[nbi][nbj] = 0
