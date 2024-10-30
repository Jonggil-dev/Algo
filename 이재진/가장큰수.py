def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*4, reverse=True)
    for i in numbers:
        answer += i
    if int(answer) == 0:
        return "0"
    return answer
