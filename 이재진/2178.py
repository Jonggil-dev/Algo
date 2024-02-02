import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
ls = [sys.stdin.readline().strip() for _ in range(N)]
distance = [[float("inf")]*M for _ in range(N)]
d_ij = [(0, 1), (-1, 0), (0, -1), (1, 0)]
pq = []
pq.append((1, (0,0)))
distance[0][0] = 1
while pq:
    w, now = heapq.heappop(pq)
    if now[0] == N-1 and now[1] == M-1:
        break
    if distance[now[0]][now[1]] >= w:
        distance[now[0]][now[1]] = w
        for d in d_ij:
            n_i, n_j = now[0] + d[0], now[1] + d[1]
            if 0 <= n_i < N and 0 <= n_j < M and ls[n_i][n_j]=="1":
                new_w = w + 1
                if distance[n_i][n_j] > new_w:
                    distance[n_i][n_j] = new_w
                    heapq.heappush(pq, (new_w, (n_i, n_j)))
print(distance[N-1][M-1])
