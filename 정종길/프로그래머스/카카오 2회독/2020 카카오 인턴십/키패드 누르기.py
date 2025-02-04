def solution(numbers, hand):
    global middle
    answer = ''
    left = { 1:(0,0), 4:(1, 0), 7:(2, 0) }
    middle = { 0:(3,1), 2:(0, 1), 5:(1, 1), 8:(2, 1)}
    right = { 3:(0, 2), 6:(1, 2), 9:(2, 2)}
    left_l, right_l = (3, 0), (3, 2)
    
    for num in numbers:
        if num in left:
            answer += "L"
            left_l = left[num]
        elif num in right:
            answer += "R"
            right_l = right[num]
        else:
            if cal_d(left_l, num) > cal_d(right_l, num):
                answer += "R"
                right_l = middle[num]
                
                
            elif cal_d(left_l, num) < cal_d(right_l, num):
                answer += "L"
                left_l = middle[num]

            else:
                if hand[0] == "r":
                    answer += "R"
                    right_l = middle[num]

                else:
                    answer += "L"
                    left_l = middle[num]
            
    return answer

def cal_d(hand, num):
    global middle
    return abs(hand[0] - middle[num][0]) + abs(hand[1] - middle[num][1])