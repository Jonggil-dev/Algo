import copy


def solution(rows, columns, queries):
    answer = []
    arr = []
    tmp = []

    for i in range(1, (rows * columns) + 1):
        tmp.append(i)
        if i % columns == 0:
            arr.append(tmp)
            tmp = []

    for querie in queries:
        x1, y1, x2, y2 = querie[0] - 1, querie[1] - 1, querie[2] - 1, querie[3] - 1
        min_v = clock_rotate(x1, y1, x2, y2, arr)
        answer.append(min_v)

    return answer


def clock_rotate(x1, y1, x2, y2, arr):
    min_value = 1e9
    lu, ru, ld, rd = arr[x1][y1], arr[x1][y2], arr[x2][y1], arr[x2][y2]

    j = y2
    while j != y1:
        num = arr[x1][j - 1]
        arr[x1][j] = num
        min_value = min(min_value, arr[x1][j])
        j -= 1

    i = x2
    while i != x1:
        if i == (x1 + 1):
            arr[i][y2] = ru
        else:
            num = arr[i - 1][y2]
            arr[i][y2] = num
        min_value = min(min_value, arr[i][y2])
        i -= 1

    j = y1
    while j != y2:
        if j == y2 - 1:
            arr[x2][j] = rd
        else:
            num = arr[x2][j + 1]
            arr[x2][j] = num
        min_value = min(min_value, arr[x2][j])
        j += 1

    i = x1
    while i != x2:
        if i == x2 - 1:
            arr[i][y1] = ld
        else:
            num = arr[i + 1][y1]
            arr[i][y1] = num
        min_value = min(min_value, arr[i][y1])
        i += 1

    return min_value

