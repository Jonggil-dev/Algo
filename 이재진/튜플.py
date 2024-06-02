def solution(s):
    answer = []
    ls = []
    length = -1
    for i in s[1:-1]:
        if i == "{":
            string = ""
        elif i == "}":
            tmp = list(map(int, list(string.split(","))))
            ls.append(tmp)
            if length < len(tmp):
                length = len(tmp)
        else:
            string += i
    for i in sorted(ls,key = lambda x:len(x)):
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer