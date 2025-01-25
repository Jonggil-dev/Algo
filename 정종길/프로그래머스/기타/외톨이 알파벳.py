def solution(input_string):
    answer = []
    for alpha in set(input_string):
        for i in range(len(input_string)):
            if input_string[i] == alpha:
                if alone_check(i, alpha, input_string):
                    answer.append(alpha)
                break
                
    if not answer:
        answer = "N"
    else:
        answer = ''.join(sorted(answer))
    return answer

def alone_check(i, alpha, input_string):
    check = i
    for j in range(i + 1, len(input_string)):
        if input_string[j] == alpha:
            if j == check + 1:
                check = j
            else:
                return True
            