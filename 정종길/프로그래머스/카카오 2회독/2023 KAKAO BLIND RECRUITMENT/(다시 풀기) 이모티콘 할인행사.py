from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discounts = product([10, 20, 30, 40], repeat = len(emoticons))
    
    for discount in discounts:
        total_pay = 0
        plus_cnt = 0
        for u_dis, u_mpay in users:            
            u_pay = 0
            for dis, price in zip(discount, emoticons):
                if dis >= u_dis:
                    u_pay += (price * (100 - dis)) // 100
            
            if u_pay >= u_mpay:
                plus_cnt += 1
            else:
                total_pay += u_pay
        
        if plus_cnt > answer[0]:
            answer[0] = plus_cnt
            answer[1] = total_pay
        elif plus_cnt == answer[0]:
            answer[1] = max(answer[1], total_pay)
        
    return answer