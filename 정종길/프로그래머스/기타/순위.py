## 부모 리스트, 자녀 리스트를 각각 만들어서 나와 연결된 부모(조상)의 수 + 자녀(손자)의 수 = 전체 인원 -1 이면 answer += 1

from collections import deque


def solution(n, results):
    global parent, child

    parent = [[] for _ in range(n + 1)]
    child = [[] for _ in range(n + 1)]

    answer = 0

    for result in results:
        parent[result[1]].append(result[0])
        child[result[0]].append(result[1])

    for i in range(1, n + 1):
        if bfs(i, n):
            answer += 1

    return answer


def bfs(i, n):
    global parent, child

    cnt = 0
    visited = [0] * (n + 1)

    q = deque([i])
    visited[i] = 1

    while q:
        node = q.popleft()
        for parent_node in parent[node]:
            if not visited[parent_node]:
                visited[parent_node] = 1
                cnt += 1
                q.append(parent_node)

    visited = [0] * (n + 1)
    q = deque([i])
    visited[i] = 1
    while q:
        node = q.popleft()
        for child_node in child[node]:
            if not visited[child_node]:
                visited[child_node] = 1
                cnt += 1
                q.append(child_node)

    if cnt == n - 1:
        return True
    else:
        return False
