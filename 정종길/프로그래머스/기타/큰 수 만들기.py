def solution(number, k):
    answer = []

    for i in range(len(number)):
        while answer and k > 0 and answer[-1] < number[i]:
            answer.pop()
            k -= 1
            if k == 0:
                break

        answer.append(number[i])

    while k > 0:
        answer.pop()
        k -= 1

    return ''.join(answer)