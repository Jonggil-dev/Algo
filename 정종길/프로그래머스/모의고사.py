def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt_ls = [0] * 3
    answer = []

    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            cnt_ls[0] += 1
        if answers[i] == second[i % 8]:
            cnt_ls[1] += 1
        if answers[i] == third[i % 10]:
            cnt_ls[2] += 1

    check = max(cnt_ls)

    for i in range(len(cnt_ls)):
        if check == cnt_ls[i]:
            answer.append(i + 1)

    return answer