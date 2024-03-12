# 프로그래머스 lv1 키패드 누르기
def solution(numbers, hand):
    keypad = {0: [3, 1], 1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0],
              8: [2, 1], 9: [2, 2]}
    L = [3, 0]
    R = [3, 2]

    answer = ''
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            L = keypad[n]
        elif n in [3, 6, 9]:
            answer += 'R'
            R = keypad[n]
        else:
            L_dist = (abs(keypad[n][0] - L[0]) + abs(keypad[n][1] - L[1]))
            R_dist = (abs(keypad[n][0] - R[0]) + abs(keypad[n][1] - R[1]))
            if L_dist < R_dist or (L_dist == R_dist and hand == 'left'):
                answer += "L"
                L = keypad[n]
            elif L_dist > R_dist or (L_dist == R_dist and hand == 'right'):
                answer += "R"
                R = keypad[n]

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'

print(solution(numbers, hand))