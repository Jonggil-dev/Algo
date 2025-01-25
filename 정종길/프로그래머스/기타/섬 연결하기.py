def solution(n, costs):
    def find_parent(node):
        if parent[node] != node:
            parent[node] = find_parent(parent[node])
        return parent[node]

    def union(x, y):
        a = find_parent(x)
        b = find_parent(y)

        if a != b:
            if a < b:
                parent[find_parent(y)] = a
            else:
                parent[find_parent(x)] = b
        return

    answer = 0
    parent = [0] * n

    for i in range(n):
        parent[i] = i

    costs.sort(key=lambda x: x[2])

    for edge in costs:
        if find_parent(edge[0]) == find_parent(edge[1]):
            continue

        union(edge[0], edge[1])
        answer += edge[2]

    return answer