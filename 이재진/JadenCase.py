def solution(s):
    answer = ''
    flag = 1
    for i in s:
        if i == " ":
            answer += " "
            flag = 1
        else:
            if flag:
                if i.isnumeric():
                    answer += i
                else:
                    answer += i.upper()
                flag = 0
            else:
                answer += i.lower()
    return answer
