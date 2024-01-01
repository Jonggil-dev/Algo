n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)] # 초기 맵 리스트
temp = [[0]*m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 바이러스를 확산하는 함수
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                #해당 위치에 바이러스 전파, 다시 재귀 수행
                temp[nx][ny] = 2
                virus(nx,ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 벽을 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    #벽이 3개 설치된 경우
    if count == 3:
        # 배열 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 바이러스 전파 시행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        # 안전 영역의 최댓값 계산
        result = max(result,get_score())
        return

    # 벽 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)