def solution(n):
    global answer

    for i in range(1, n + 1):
        sum_seq(i, n)

    return answer


def sum_seq(start, n):
    global answer
    tot = 0

    for i in range(start, n + 1):
        tot += i
        if tot > n:
            return

        elif tot == n:
            answer += 1
            return


answer = 0




