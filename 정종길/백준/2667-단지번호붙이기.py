def dfs(x, y):

    if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] == 0:
        return 0

    graph[x][y] = 0
    count = 1
    count += dfs(x+1, y)
    count += dfs(x-1, y)
    count += dfs(x, y+1)
    count += dfs(x, y-1)
    return count

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(dfs(i, j))

result.sort()
print(len(result))
for r in result:
    print(r)
