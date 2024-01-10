# 프로그래머스 행렬 테투리 회전하기

def solution(rows, columns, queries):
    answer = []
    init = [[(columns*j) + i for i in range(1, columns+1)] for j in range(0, rows)]
    #print(init)
    for a, b, c, d in queries:
        x1, y1, x2, y2 = a-1, b-1, c-1, d-1
        now = init[x1][y1]
        MIN = now
        # 시작 지점부터 오른쪽으로
        for ny in range(y1, y2 + 1):
            next = init[x1][ny]
            # print('a', x1, ny)
            init[x1][ny] = now
            now = next
            # print(now)
            MIN = min(now, MIN)
        # 오른쪽 위 꼭짓점에서 아래쪽으로
        for nx in range(x1+1, x2+1):
            # print('b', nx, y2)
            next = init[nx][y2]
            init[nx][y2] = now
            now = next
            # print(now)
            MIN = min(now, MIN)
        # 오른쪽 아래 꼭짓점에서 왼쪽으로
        for ny in range(y2-1, y1-1, -1):
            # print('c', x2, ny)
            next = init[x2][ny]
            init[x2][ny] = now
            now = next
            # print(now)
            MIN = min(now, MIN)
        # 왼쪽 아래 꼭짓점에서 위로
        for nx in range(x2-1, x1, -1):
            # print('d', nx, y1)
            next = init[nx][y1]
            init[nx][y1] = now
            now = next
            # print(now)
            MIN = min(now, MIN)
        answer.append(MIN)

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# rows = 3
# columns = 3
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
# rows = 100
# columns = 97
# queries = [[1,1,100,97]]
rows= 5
columns = 5
queries = [[2, 3, 4, 5], [2, 3, 4, 5], [2, 3, 4, 5], [2, 3, 4, 5]]
rows= 3
columns = 4
queries = [[1, 1, 2, 2], [1, 2, 2, 3], [1, 3, 2, 4], [2, 3, 3, 4]]
rows= 3
columns = 5
queries = [[1, 1, 2, 2], [2, 3, 3, 4], [1, 2, 3, 4], [1, 1, 3, 4], [2, 2, 3, 5]]
rows= 6
columns = 6
queries = [[2, 2, 5, 3]]
print(solution(rows, columns, queries))