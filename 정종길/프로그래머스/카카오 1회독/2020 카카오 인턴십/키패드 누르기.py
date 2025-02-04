def solution(numbers, hand):
    global dict_
    
    answer = ''
    dict_ = {
        '1' : (0, 0), '2' : (0, 1), '3' : (0, 2), 
        '4' : (1, 0), '5' : (1, 1), '6' : (1, 2), 
        '7' : (2, 0), '8' : (2, 1), '9' : (2, 2), 
        '*' : (3, 0), '0' : (3, 1), '#' : (3, 2)
    }
    
    left, right = '*', '#'

    for num in numbers:
        res = dist(left, right, num, hand)
        if  res == "L":
            left = num
        else:
            right = num
        answer += res
        
    return answer

def dist(left, right, num, hand):
    global dict_
    
    
    if num in (1, 4, 7):
        return "L"
    
    elif num in (3, 6, 9):
        return "R"
    
    left, right, num = dict_[str(left)], dict_[str(right)], dict_[str(num)]
    ld = abs(num[0] - left[0]) + abs(num[1] - left[1])
    rd = abs(num[0] - right[0]) + abs(num[1] - right[1])

    if ld > rd:
        return "R"
    elif rd > ld:
        return "L"
    else:
        if hand == "right":
            return "R"
        else:
            return "L"