# 프로그래머스 Lv2 숫자블록

# n번째 자리에 들어갈 블록의 숫자는 n의 약수 중 자기 자신을 제외한 가장 큰 수의 블록임
# 주의사항: 블록 칸의 수는 1 ~ 1,000,000,000 이고 블록은 1 ~ 10,000,000 번 까지 존재함

import math

def solution(begin, end):
    def find_number(n):
        MAX = 0
        for i in range(2, int(math.sqrt(n)+1)): # 루트(n)보다 작은 수 중 n의 약수는 되지만 n/(약수)가 10,000,000이 넘는 경우가 있음
            if n % i == 0:
                MAX = i # 모든 n/(약수)가 10,000,000이 넘는다면, 지금까지 구한 약수 중 가장 큰 수가 "n번째 자리에 놓이는 블록의 숫자"가 됨
                if n/i <= 10000000: #n/(약수)가 10,000,000이 넘지 않으면, 그게 약수 중 가장 큰 수가 됨
                    return int(n/i)
        else:
            return max(1, MAX)

    answer = []

    for n in range(begin, end+1):
        if n == 1:
            answer.append(0)
        else:
            answer.append(find_number(n))
    return answer


print(solution(1, 10))
print(solution(999999990, 1000000000))
