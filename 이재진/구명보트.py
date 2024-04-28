def solution(people, limit):
    answer = 0
    left = 0
    people.sort()
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        elif left == right:
            answer += 1
            break
        else:
            answer += 1
            right -= 1
    return answer
