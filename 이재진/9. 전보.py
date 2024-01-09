import sys
import heapq
n, m, c = map(int, sys.stdin.readline().split())
ls = [[] for _ in range(n+1)]
for _ in range(m):
    # 출발, 도착, 가중치(시간)
    x, y, z = map(int, sys.stdin.readline().split())
    ls[x].append([y, z])
def dijkstra(start, end):
    pq = []
    distance = [float("inf")] * (n + 1)
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        weight, now = heapq.heappop(pq)
        if now == end:
            return distance[now]
        if distance[now] >= weight:
            for next, w in ls[now]:
                new_weight = weight + w
                if distance[next] > new_weight + weight:
                    distance[next] = new_weight + weight
                    heapq.heappush(pq, (new_weight, next))
    return -1
total_time = 0
cnt = 0
for i in range(1, n+1):
    if i != c:
        tmp = dijkstra(c, i)
        if tmp != -1:
            total_time = max(total_time, tmp)
            cnt += 1
print(cnt, total_time)