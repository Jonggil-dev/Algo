import heapq


def solution(n, edge):
    distance = [1e9] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for n1, n2 in edge:
        graph[n1].append((n2, 1))
        graph[n2].append((n1, 1))

    task = [(0, 1)]
    distance[1] = 0

    while task:

        min_dist, now = heapq.heappop(task)

        if min_dist > distance[now]:
            continue

        for node, cost in graph[now]:
            next_dist = min_dist + cost

            if distance[node] > (next_dist):
                distance[node] = (next_dist)
                heapq.heappush(task, (next_dist, node))

    distance.sort(reverse=True)

    for check in distance:
        if check != 1e9:
            mv = check
            break

    answer = distance.count(mv)

    return answer


