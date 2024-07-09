def solution(arr):
    # 결과를 저장할 변수 (0의 개수, 1의 개수)
    result = [0, 0]

    # 주어진 배열을 재귀적으로 처리하는 함수
    def compress(x, y, n):
        # 시작점의 값 (모든 값이 이 값과 같아야 함)
        start = arr[x][y]
        # 현재 구역을 전부 검사
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != start:
                    # 값이 다르면 현재 구역을 4분할하여 재귀 호출
                    half = n // 2
                    compress(x, y, half)
                    compress(x, y + half, half)
                    compress(x + half, y, half)
                    compress(x + half, y + half, half)
                    return

        # 모든 값이 같으면 해당 값을 카운트
        if start == 0:
            result[0] += 1
        else:
            result[1] += 1

    # 전체 영역에 대해 함수 호출
    compress(0, 0, len(arr))

    return result
