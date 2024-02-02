# 프로그래머스 Lv1 콜라츠 추측

# 주어진 수가 1이 될 때까지 다음 작업을 반복하면 모든 수를 1로 만들 수 있다는 추측
# 입력된 수가 짝수라면 2로 나눈다
# 입력된 수가 홀수라면 3을 곱하고 1을 더한다
# 1이 될 때까지 반복

# 몇번 반복해야 1이 되는지 구하라.
# 주어진 수가 1이면 0, 500번 이상 반복해야하면 -1

def solution(num):
    if num == 1:
        return 0

    answer = 0
    while num != 1 and answer < 500:
        if num % 2 == 0: # 짝수면
            num //= 2
            answer += 1
        else:
            num = num * 3 + 1
            answer += 1

    return answer if num == 1 else -1

print(solution(6))
print(solution(16))
print(solution(626331))