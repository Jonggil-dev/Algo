# 프로그래머스 하노이의 탑

# 핵심은 재귀!
# https://shoark7.github.io/programming/algorithm/tower-of-hanoi 참고함

def solution(n):
    answer = []
    def hanoi(N, start, to, via):
        if N == 1:
            answer.append([start, to])
            return
        hanoi(N-1, start, via, to)
        answer.append([start, to])
        hanoi(N-1, via, to, start)

    hanoi(n, 1, 3, 2)
    return answer

n = 2
print(solution(n))