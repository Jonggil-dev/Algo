def solution(n, words):
    check = {words[0]}
    for i in range(1, len(words)):
        if (words[i - 1][-1] != words[i][0]) or (words[i] in check):
            person = (i % n) + 1
            stage = (i // n) + 1
            answer = [person, stage]
            return answer

        check.add(words[i])

    answer = [0, 0]
    return answer