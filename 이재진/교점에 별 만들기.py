from itertools import combinations

def cal(x, y):
    A, B, E = x
    C, D, F = y
    denominator = A * D - B * C
    if denominator == 0:
        return False
    
    x_coord = (B * F - E * D) / denominator
    y_coord = (E * C - A * F) / denominator
    
    if x_coord.is_integer() and y_coord.is_integer():
        return [int(x_coord), int(y_coord)]
    else:
        return False

def solution(line):
    points = []
    min_i, min_j = float("inf"), float("inf")
    max_i, max_j = float("-inf"), float("-inf")
    
    for line1, line2 in combinations(line, 2):
        point = cal(line1, line2)
        if point:
            x, y = point
            points.append((x, y))
            min_i, min_j = min(min_i, x), min(min_j, y)
            max_i, max_j = max(max_i, x), max(max_j, y)
    
    width, height = max_i - min_i + 1, max_j - min_j + 1
    grid = [["."] * width for _ in range(height)]
    
    for x, y in points:
        grid[max_j - y][x - min_i] = "*"
    
    return ["".join(row) for row in grid]
