def solution(prices):
    answer = []

    for i in range(len(prices)):
        time = 0
        for j in range(i + 1, len(prices)):
            time += 1
            if prices[i] > prices[j]:
                answer.append(time)
                break
        else:
            answer.append(time)
    return answer