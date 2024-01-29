# 프로그래머스 Lv2 숫자 카드 나누기
import math

# arrayA의 약수 중 arrayB를 나눌 수 없거나
# arrayB의 약수 중 arrayA를 나눌 수 없는 숫자 a 중 가장 큰 값, 없으면 0
def solution(arrayA, arrayB):
    answer = 0
    gcd_A = arrayA[0]
    gcd_B = arrayB[0]
    i = 1
    while i < len(arrayA):
        gcd_A = math.gcd(gcd_A, arrayA[i])
        gcd_B = math.gcd(gcd_B, arrayB[i])
        i += 1

    if gcd_A == 1 and gcd_B == 1:
        return 0

    div_A = []
    div_B = []
    if gcd_A != 1:
        a = 2
        while a < (gcd_A)**(1/2):
            if gcd_A % a == 0:
                div_A.extend([a, gcd_A//a])
            a += 1
        div_A.append(gcd_A)
    if gcd_B != 1:
        b = 2
        while b < (gcd_B)**(1/2):
            if gcd_B % b == 0:
                div_B.extend([b, gcd_B//b])
            b += 1
        div_B.append(gcd_B)

    # print(div_A, div_B)
    while div_A:
        tmp = div_A.pop()
        if all([i % tmp != 0 for i in arrayB]):
            answer = max(answer, tmp)

    while div_B:
        tmp = div_B.pop()
        if all([i % tmp != 0 for i in arrayA]):
            answer = max(answer, tmp)

    return answer

arrayA = [10, 17]
arrayB = [5, 20]
arrayA = [10, 20]
arrayB = [5, 17]
# arrayA = [14, 35, 119]
# arrayB = [18, 30, 102]
print(solution(arrayA, arrayB))
