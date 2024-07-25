def solution(commands):
    global answer, parents, arr
    answer = []
    parents = [[(i, j) for j in range(51)] for i in range(51)]
    arr = [[0] * 51 for _ in range(51)]

    for command in commands:
        li = command.split()
        if li[0] == "UPDATE":
            if len(li) == 4:
                update1(int(li[1]), int(li[2]), li[3])
            else:
                update2(li[1], li[2])

        elif li[0] == "MERGE":
            merge(int(li[1]), int(li[2]), int(li[3]), int(li[4]))


        elif li[0] == "UNMERGE":
            unmerge(int(li[1]), int(li[2]))

        else:
            show(int(li[1]), int(li[2]))

    return answer


def find_parent(r, c):
    global parents, arr
    if parents[r][c] != (r, c):
        parents[r][c] = find_parent(parents[r][c][0], parents[r][c][1])
    return parents[r][c]


def update1(r, c, v):
    global parents, arr
    nr, nc = find_parent(r, c)
    arr[nr][nc] = v
    return


def update2(v1, v2):
    global parents, arr
    for i in range(1, 51):
        for j in range(1, 51):
            if arr[i][j] == v1:
                arr[i][j] = v2
    return


def merge(r1, c1, r2, c2):
    global parents, arr

    pr1, pc1 = find_parent(r1, c1)
    pr2, pc2 = find_parent(r2, c2)

    if (pr1, pc1) < (pr2, pc2):
        parents[pr2][pc2] = (pr1, pc1)
        if not arr[pr1][pc1] and arr[pr2][pc2]:
            arr[pr1][pc1] = arr[pr2][pc2]
    else:
        parents[pr1][pc1] = (pr2, pc2)
        if (not arr[pr2][pc2] and arr[pr1][pc1]) or (arr[pr2][pc2] and arr[pr1][pc1]):
            arr[pr2][pc2] = arr[pr1][pc1]
    return


def unmerge(r, c):
    global parents, arr
    for i in range(1, 51):
        for j in range(1, 51):
            find_parent(i, j)
    nr, nc = find_parent(r, c)
    tmp = arr[nr][nc]

    for i in range(1, 51):
        for j in range(1, 51):
            if parents[i][j] == (nr, nc):
                parents[i][j] = (i, j)
                arr[i][j] = 0

    arr[r][c] = tmp
    return


def show(r, c):
    global answer, arr
    nr, nc = find_parent(r, c)
    if arr[nr][nc]:
        answer.append(arr[nr][nc])
    else:
        answer.append("EMPTY")
    return