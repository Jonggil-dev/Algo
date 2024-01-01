# 프로그래머스 배달

def solution(N, roads, K):
    adj_arr = [[float("inf")] * (N+1) for _ in range(N+1)]
    for road in roads:
        # 무방향 그래프
        adj_arr[road[0]][road[1]] = min(road[2], adj_arr[road[0]][road[1]])
        adj_arr[road[1]][road[0]] = min(road[2], adj_arr[road[1]][road[0]])

    visited = [-1] * (N+1)
    queue = [1]
    visited[1] = 0

    while queue:
        now = queue.pop(0)
        for next in range(2, N+1):
            if now != next and adj_arr[now][next] != float("inf"):
                if visited[next] != -1 and visited[next] < visited[now] + adj_arr[now][next]:
                    continue

                visited[next] = visited[now] + adj_arr[now][next]
                queue.append(next)

    # print(visited)
    answer = 0
    for i in range(K+1):
        answer += visited.count(i)
    return answer


N = 5
roads = [[1,2,1], [2,3,3], [5,2,2], [1,4,2], [5,3,1], [5,4,2]]
K = 3

N = 6
roads = [[1,2,1], [1,3,2], [2,3,2], [3,4,3], [3,5,2], [3,5,3], [5,6,1]]
K = 4

print(solution(N, roads, K))
