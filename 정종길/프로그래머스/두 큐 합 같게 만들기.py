from collections import deque


def solution(queue1, queue2):
    answer = -1
    cnt = 0
    N = len(queue1)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    a = sum(queue1)
    b = sum(queue2)

    while cnt <= (3 * N - 3):
        if a == b:
            return cnt

        elif a > b:
            num = queue1.popleft()
            queue2.append(num)
            a -= num
            b += num

        else:
            num = queue2.popleft()
            queue1.append(num)
            b -= num
            a += num

        cnt += 1

    return answer

