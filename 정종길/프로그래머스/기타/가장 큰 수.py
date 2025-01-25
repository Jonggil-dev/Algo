def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x:x*4, reverse=True)
    answer=str(int(''.join(numbers)))

    return answer