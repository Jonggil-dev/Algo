import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 각 노드의 깊이, 최소 공통 조상, 거리를 저장할 배열
depth = [0] * (N + 1)
dp = [[0, 0] for _ in range(N + 1)]  # [조상, 거리]
visited = [False] * (N + 1)

def dfs(x, d, dist):
    visited[x] = True
    depth[x] = d
    for next, distance in graph[x]:
        if not visited[next]:
            dp[next][0] = x  # 바로 위의 조상
            dp[next][1] = dp[x][1] + distance  # 루트부터 현재 노드까지의 거리
            dfs(next, d + 1, dist + distance)

dfs(1, 0, 0)  # 루트 노드에서 시작하여 DFS 실행

def lca(a, b):
    # 두 노드의 깊이가 동일하도록 조정
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = dp[a][0]
        else:
            b = dp[b][0]
    # 공통 조상을 찾을 때까지 두 노드를 동시에 위로 올림
    while a != b:
        a = dp[a][0]
        b = dp[b][0]
    return a

for _ in range(M):
    a, b = map(int, input().split())
    ancestor = lca(a, b)
    # 두 노드 사이의 거리 계산
    distance = dp[a][1] + dp[b][1] - 2 * dp[ancestor][1]
    print(distance)
