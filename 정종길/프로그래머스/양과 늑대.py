from collections import deque


def solution(info, edges):
    global answer, graph
    n = len(info)
    answer = 0
    graph = [[] for _ in range(n)]

    for p, c in edges:
        graph[p].append(c)

    bfs(info)

    return answer


def bfs(info):
    global answer, graph

    q = deque([(0, 1, 0, graph[0])])

    while q:
        now, sheep, wolf, next_ = q.popleft()
        for i in next_:
            if info[i]:
                if wolf + 1 >= sheep:
                    continue
                else:
                    nnext_ = next_[:]
                    nnext_.remove(i)
                    q.append((i, sheep, wolf + 1, nnext_ + graph[i]))
            else:
                nnext_ = next_[:]
                nnext_.remove(i)
                q.append((i, sheep + 1, wolf, nnext_ + graph[i]))

        answer = max(answer, sheep)