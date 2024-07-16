import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    distance = [1e9] * (n + 1)
    is_summit = [0] * (n + 1)

    for summit in summits:
        is_summit[summit] = 1

    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    for gate in gates:
        daik(gate, distance, is_summit, graph)

    min_v = 1e9
    for summit in sorted(summits):
        if min_v > distance[summit]:
            min_v = distance[summit]
            answer = [summit, distance[summit]]

    return answer


def daik(node, distance, is_summit, graph):
    q = [(0, node)]
    distance[node] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now] or is_summit[now]:
            continue

        for node, weight in graph[now]:
            max_weight = max(distance[now], weight)
            if distance[node] > max_weight:
                distance[node] = max_weight
                heapq.heappush(q, (weight, node))

