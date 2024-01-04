# 프로그래머스 거리두기 확인하기

def solution(places):
    outer = [[0, 2], [2, 0]]
    diag = [[1, 1], [1, -1]]
    inner = [[0, 1], [1, 0]]
    def distance_check(i, j, place):
        # 2칸 아래, 위, 좌, 우에 P 있는지 확인 -> 있으면 중심과 P 사이 X 있는지 확인
        for di, dj in outer:
            ni, nj = i + di, j + dj
            if (0 <= ni < 5) and (0 <= nj < 5) and place[ni][nj] == 'P':
                if place[i + (di//2)][j + (dj//2)] != 'X':
                    return 0
        # 대각선 1칸 거리에 P 있는지 확인 -> 있으면 중심과 P 사이 X 있는지 확인(2개)
        for di, dj in diag:
            ni, nj = i + di, j + dj
            if (0 <= ni < 5) and (0 <= nj < 5) and place[ni][nj] == 'P':
                if place[i][nj] != 'X' or place[ni][j] != 'X':
                    return 0
        # 상하좌우에 P 있는지 확인
        for di, dj in inner:
            ni, nj = i + di, j + dj
            if (0 <= ni < 5) and (0 <= nj < 5) and place[ni][nj] == 'P':
                return 0
        return 1

    answer = []
    for place in places:
        flag = 1
        for row in range(5):
            if flag == 0:
                break
            for col in range(5):
                if place[row][col] == 'P':
                    flag = distance_check(row, col, place)
                    if flag == 0:
                        break
        answer.append(flag)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))


