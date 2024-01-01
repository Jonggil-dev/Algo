# 큰 수 만들기_프로그래머스

from collections import deque

def solution(number, k):
    if len(set(number)) == 1:
        return number[:len(number)-k]

    right = deque(list(number))
    left = deque()

    while k > 0:
        if list(right) == sorted(right, reverse=True):
            right = list(right)
            return ''.join(right[:len(right)-k])

        while len(right) >= 2:
            if k == 0:
                break
            # print(number)
            if right[0] < right[1]:
                k -= 1
                right.popleft()
                if left:
                    right.appendleft(left.pop())

            else:
                left.append(right.popleft())

        right = left + right
        left = deque()

    answer = ''.join(left) + ''.join(right)
    return answer

# number = '1924'
# k = 2
# number = '1231234'
# k = 3
# number = '1122'
# k = 2
# number = '4177252841'
# k = 4
# number = '111'
# k = 1
# number = '4321'
# k = 2
# number = '909090'
# k = 5
# number = '720378'
# k = 2
print(solution(number, k))


# 10번 테스트 케이스 시간 초과

def solution(number, k):
    front = ''
    back = ''
    if len(set(number)) == 1:
        return number[:len(number)-k]
    if number.count('9') == len(number) - k:
        return '9' * (len(number) - k)

    while k > 0:
        if len(number) == k:
            number = ''
            break

        max_idx = number.find(max(number)) # 가장 큰 수의 인덱스(중복 있으면 앞에거)
        # print('max: ', max_idx)
        if max_idx <= k:
            front += number[max_idx]
            number = number[max_idx+1:]
            k -= max_idx
        else:
            back = number[max_idx:] + back
            number = number[:max_idx]

    return front + number + back# 큰 수 만들기_프로그래머스

from collections import deque

def solution(number, k):
    if len(set(number)) == 1:
        return number[:len(number)-k]

    right = deque(list(number))
    left = deque()

    while k > 0:
        if list(right) == sorted(right, reverse=True):
            right = list(right)
            return ''.join(right[:len(right)-k])

        while len(right) >= 2:
            if k == 0:
                break
            # print(number)
            if right[0] < right[1]:
                k -= 1
                right.popleft()
                if left:
                    right.appendleft(left.pop())

            else:
                left.append(right.popleft())

        right = left + right
        left = deque()

    answer = ''.join(left) + ''.join(right)
    return answer

# number = '1924'
# k = 2
# number = '1231234'
# k = 3
# number = '1122'
# k = 2
# number = '4177252841'
# k = 4
# number = '111'
# k = 1
# number = '4321'
# k = 2
# number = '909090'
# k = 5
# number = '720378'
# k = 2
print(solution(number, k))


# 10번 테스트 케이스 시간 초과

def solution(number, k):
    front = ''
    back = ''
    if len(set(number)) == 1:
        return number[:len(number)-k]
    if number.count('9') == len(number) - k:
        return '9' * (len(number) - k)

    while k > 0:
        if len(number) == k:
            number = ''
            break

        max_idx = number.find(max(number)) # 가장 큰 수의 인덱스(중복 있으면 앞에거)
        # print('max: ', max_idx)
        if max_idx <= k:
            front += number[max_idx]
            number = number[max_idx+1:]
            k -= max_idx
        else:
            back = number[max_idx:] + back
            number = number[:max_idx]

    return front + number + back