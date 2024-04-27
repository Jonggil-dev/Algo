# 프로그래머스 lv2 교점에 별 만들기

from itertools import combinations as comb

def solution(line):
    intersection = []
    min_x = float("inf")
    max_x = float("inf") * (-1)
    min_y = float("inf")
    max_y = float("inf") * (-1)
    for line1, line2 in comb(line, 2):
        if line1[0] * line2[1] - line1[1] * line2[0] == 0:
            continue
        
        x = (line1[1] * line2[2] - line1[2] * line2[1]) / (line1[0] * line2[1] - line1[1] * line2[0])
        y = (line1[2] * line2[0] - line1[0] * line2[2]) / (line1[0] * line2[1] - line1[1] * line2[0])
        if x == int(x) and y == int(y) and [int(x), int(y)] not in intersection:
            min_x = min(min_x, int(x))
            max_x = max(max_x, int(x))
            min_y = min(min_y, int(y))
            max_y = max(max_y, int(y))
            intersection.append([int(x), int(y)])

    tmp = [["."] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for point in intersection:
        tmp[point[1] - min_y][point[0] - min_x] = "*"

    answer = [''.join(tmp[i]) for i in range(max_y - min_y + 1)]
    return answer[::-1]

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
line = [[1, -1, 0], [2, -1, 0]]
line = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]

print(solution(line))