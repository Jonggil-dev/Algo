# Baekjoon 1389번 케빈 베이컨의 6단계 법칙

import sys
from collections import deque

def BFS(start):
  dist = dist_arr[start]
  queue = deque()
  queue.append(start)

  while queue:
    now = queue.pop()

    for next in range(N):
      if adj_arr[now][next] == 1 and (dist[next] == 0 or dist[next] > dist[now] + 1) and next != start:
        dist[next] = dist[now] + 1
        queue.append(next)


input = sys.stdin.readline

N, M = map(int, input().split())
# 양방향 그래프
adj_arr = [[0] * N for _ in range(N)]


for _ in range(M):
  a, b = map(int, input().split())
  adj_arr[a-1][b-1] = 1
  adj_arr[b-1][a-1] = 1


dist_arr = [[0] * N for _ in range(N)] # 각 포인트에서 다른 포인트로 가는 최소 거리 저장

MIN = float("inf")
for i in range(N):
  BFS(i)
  if MIN > sum(dist_arr[i]):
    MIN = min(MIN, sum(dist_arr[i]))
    answer = i


print(answer+1)



