import sys

sys.setrecursionlimit(1000000)


def solution(edges):
    global answer, out_graph, in_graph, visited

    answer = [0] * 4
    out_graph = [[] for _ in range(1000001)]
    in_graph = [[] for _ in range(1000001)]

    visited = set()

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
        visited.add(node)
        dfs(node)

    return answer


def dfs(i):
    global answer, out_graph, in_graph, visited

    if not out_graph[i]:
        answer[2] += 1
        return True

    if len(out_graph[i]) == 2 and (len(in_graph[i]) == 2 or len(in_graph[i]) == 3):
        answer[3] += 1
        return True

    for node in out_graph[i]:
        if node in visited:
            answer[1] += 1
            return True

        visited.add(node)
        if dfs(node):
            return True
