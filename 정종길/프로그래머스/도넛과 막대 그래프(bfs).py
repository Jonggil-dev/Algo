from collections import deque


def solution(edges):
    global answer, out_graph, visited

    answer = [0] * 4
    out_graph = [[] for _ in range(1000001)]
    in_graph = [[] for _ in range(1000001)]

    for start, end in edges:
        out_graph[start].append(end)
        in_graph[end].append(start)

    for i, node in enumerate(out_graph):
        if len(node) >= 3:
            make_node = i
            break

        elif len(node) == 2:
            if not in_graph[i]:
                make_node = i
                break

    answer[0] = make_node

    for node in out_graph[make_node]:
        bfs(node)

    return answer


def bfs(i):
    global answer, out_graph, visited

    q = deque([i])
    visited = {i}
    cnt_node = 0
    cnt_edge = 0

    while q:
        now = q.popleft()
        cnt_node += 1

        for node in out_graph[now]:
            cnt_edge += 1
            if node not in visited:
                visited.add(node)
                q.append(node)

    if cnt_node == cnt_edge:
        answer[1] += 1

    elif cnt_node - 1 == cnt_edge:
        answer[2] += 1

    elif cnt_edge == 0:
        answer[2] += 1

    else:
        answer[3] += 1

