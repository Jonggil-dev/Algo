import heapq

d_ij = [(0,1), (1,0), (0,-1), (-1,0)]
def dijkstra(x):
    pq = []
    heapq.heappush(pq, (0, x))
    distance[x[0]][x[1]] = 0
    while pq:
        weight, now = heapq.heappop(pq)
        if now[0]+1 == N and now[1]+1 == M:
            return weight
        if distance[now[0]][now[1]] >= weight:
            distance[now[0]][now[1]] = weight
            for d in d_ij:
                ni, nj = now[0]+d[0], now[1]+d[1]
                if 0<=ni<N and 0<=nj<M and ls[ni][nj] == 1:
                    new_weight = weight + 1
                    if distance[ni][nj] > new_weight:
                        distance[ni][nj] = new_weight
                        heapq.heappush(pq, (new_weight,(ni, nj)))


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ls = [list(map(int, list(input()))) for _ in range(N)]
    distance = [[float("inf")]*M for _ in range(N)]
    dijkstra((0,0))
    res = distance[N-1][M-1] + 1
    print(f'#{t}', res)