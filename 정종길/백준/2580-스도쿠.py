def is_valid(row, col, num):
    # 행 검사
    if num in Arr[row]:
        return False

    # 열 검사
    for i in range(9):
        if num == Arr[i][col]:
            return False

    # 3x3 서브그리드 검사
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if Arr[startRow + i][startCol + j] == num:
                return False
    return True

def sudoku(index):
    if index == len(checkNode):
        return True

    i, j = checkNode[index]
    for num in range(1, 10):
        if is_valid(i, j, num):
            Arr[i][j] = num
            if sudoku(index + 1):
                return True
            Arr[i][j] = 0
    return False

Arr = [list(map(int, input().split())) for _ in range(9)]
checkNode = []

for i in range(9):
    for j in range(9):
        if Arr[i][j] == 0:
            checkNode.append((i,j))

if sudoku(0):
    for row in Arr:
        print(' '.join(map(str, row)))
