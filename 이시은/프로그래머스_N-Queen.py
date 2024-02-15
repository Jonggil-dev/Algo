# 프로그래머스 N-Queen

# Queen 은 가로, 세로, 대각선으로 움직일 수 있다
# Queen이 서로 한번에 공격할 수 없는 위치에 배치할 수 있는 방법의 수를 구하라
#
# => 이전에 놓은 곳과 같은 열, 대각선에 놓을 수 없음

def solution(n):
    answer = 0
    row = [0] * n

    def Queen(x):
        nonlocal row, answer
        if x == n:
            # print(row)
            answer += 1
            return

        for y in range(n):
            row[x] = y
            for i in range(x):
                # 위의 행에서 y 열에 퀸을 놓은 적이 있거나 대각선 위쪽에 퀸이 있는지 확인
                if row[i] == y or abs((x - i) / (y - row[i])) == 1:
                    break
            else:
                Queen(x+1)
    Queen(0)

    return answer

print(solution(5))
