def solution(s):
    answer = ''
    dict_ = {
        "zero":'0', "one" : '1', "two" : '2', "three" : '3', "four" : '4', "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'
    }
    
    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer += s[i]
            i += 1
            continue
        else:
            for j in range(i + 3, len(s) + 1):
                if s[i:j] in dict_.keys():
                    answer += dict_[s[i:j]]
                    i = j
                    break
                    
    return int(answer)