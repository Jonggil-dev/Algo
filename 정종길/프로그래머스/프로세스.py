from collections import deque


def solution(priorities, location):
    priorities = deque(priorities)
    N = len(priorities)
    answer = 0
    idx = -1

    while True:
        flag = True
        idx = (idx + 1) % N

        if not priorities:
            return N

        process = priorities.popleft()

        if process == -1:
            priorities.append(-1)
            continue

        for check in priorities:
            if process < check:
                priorities.append(process)
                flag = False
                break

        if flag:
            answer += 1
            priorities.append(-1)
            if idx == location:
                return answer


