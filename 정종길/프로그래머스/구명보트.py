from collections import deque


def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)

    answer = 0
    while people:
        total = people.popleft()
        if people and (total + people[-1]) <= limit:
            total += people.pop()
        answer += 1

    return answer