def solution(commands):
    answer = []
    graph = [[0] * 51 for _ in range(51)]
    merge_info = [[(0, 0)] for _ in range(51)]

    for i in range(1, 51):
        for j in range(1, 51):
            merge_info[i].append((i, j))

    for command in commands:
        co = list(command.split())

        if co[0] == "UPDATE":
            if len(co) == 4:
                r, c = find_merge(merge_info, int(co[1]), int(co[2]))
                graph[r][c] = co[3]
            else:
                for i in range(1, 51):
                    for j in range(1, 51):
                        if graph[i][j] == co[1]:
                            graph[i][j] = co[2]

        elif co[0] == "MERGE":
            a, b = find_merge(merge_info, int(co[1]), int(co[2]))
            c, d = find_merge(merge_info, int(co[3]), int(co[4]))
            merge(merge_info, graph, a, b, c, d)

        elif co[0] == "UNMERGE":
            a, b = find_merge(merge_info, int(co[1]), int(co[2]))
            if graph[a][b]:
                v = graph[a][b]
                unmerge(merge_info, graph, a, b)
                graph[int(co[1])][int(co[2])] = v
            else:
                unmerge(merge_info, graph, a, b)

        elif co[0] == "PRINT":
            a, b = find_merge(merge_info, int(co[1]), int(co[2]))
            ans = graph[a][b]
            if not ans:
                answer.append("EMPTY")
            else:
                answer.append(ans)

    # for i in range(1, 5):
    #     print(graph[i][1:5])
    # for i in range(1, 5):
    #     print(merge_info[i][1:5])
    return answer


def find_merge(merge_info, r, c):
    if merge_info[r][c] != (r, c):
        merge_info[r][c] = find_merge(merge_info, merge_info[r][c][0], merge_info[r][c][1])
    return merge_info[r][c]


def merge(merge_info, graph, r1, c1, r2, c2):
    a, b = find_merge(merge_info, r1, c1)
    c, d = find_merge(merge_info, r2, c2)

    v1, v2 = graph[a][b], graph[c][d]

    if (a, b) <= (c, d):
        merge_info[c][d] = (a, b)
        if v1 and v2:
            graph[a][b] = v1
        elif v1 and not v2:
            graph[a][b] = v1
        elif not v1 and v2:
            graph[a][b] = v2

    else:
        merge_info[a][b] = (c, d)
        if v1 and v2:
            graph[c][d] = v1
        elif v1 and not v2:
            graph[c][d] = v1
        elif not v1 and v2:
            graph[c][d] = v2


def unmerge(merge_info, graph, a, b):
    for i in range(1, 51):
        for j in range(1, 51):
            find_merge(merge_info, i, j)

    for i in range(1, 51):
        for j in range(1, 51):
            if merge_info[i][j] == (a, b):
                merge_info[i][j] = (i, j)
                graph[i][j] = 0
