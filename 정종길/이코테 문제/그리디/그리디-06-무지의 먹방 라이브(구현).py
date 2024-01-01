'''
설계
1. k를 하나씩 줄여가면서 0이 될 때 food_times의 인덱스
'''


def solution(food_times, k):
    answer = 0
    food_len = len(food_times)

    while:
        if k == -1:
            return answer

        if not food_times[answer]:
            continue

        else:
            food_times[answer] -= 1
            k -= 1
            answer += 1

            if answer >= food_len - 1:
                answer %= food_len
