##사각형의 변을 1로 먼저 그리고, 내부 영역은 그냥 2로 색칠하면 Arr 완성됨
##연달아 붙어있는 사각형의 경우 dfs 진행 시 정확한 경로가 어딘지 구분을 못함으로
## 처음부터 모든 좌표를 x2 한다음 return할 때 이동한 경로의 값을 2로 나눠서 처리하기

def solution(rectangle, characterX, characterY, itemX, itemY):
    global arr, answer

    answer = 1e9
    arr = [[0] * 101 for _ in range(101)]
    for square in rectangle:
        draw_arr(square[0] * 2, square[1] * 2, square[2] * 2, square[3] * 2)

    arr[itemX * 2][itemY * 2] = 3
    dfs(characterX * 2, characterY * 2, 0)

    return answer


def draw_arr(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        if not arr[x][y1]:
            arr[x][y1] = 1

        if not arr[x][y2]:
            arr[x][y2] = 1

    for y in range(y1, y2 + 1):
        if not arr[x1][y]:
            arr[x1][y] = 1

        if not arr[x2][y]:
            arr[x2][y] = 1

    for y in range(y1 + 1, y2):
        for x in range(x1 + 1, x2):
            arr[x][y] = 2


def dfs(i, j, cnt):
    global answer
    if arr[i][j] == 3:
        answer = min(answer, cnt // 2)
        return

    arr[i][j] = 2
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj
        if 0 <= ni <= 100 and 0 <= nj <= 100:
            if arr[ni][nj] == 1 or arr[ni][nj] == 3:
                dfs(ni, nj, cnt + 1)



