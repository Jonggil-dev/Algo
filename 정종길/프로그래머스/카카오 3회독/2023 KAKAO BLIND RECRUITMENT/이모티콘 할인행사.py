from itertools import product

def solution(users, emoticons):
    answer = [-1, -1]

    discnts = [10, 20, 30, 40]
    discnt_info = product(discnts, repeat = len(emoticons))
    
    for li in discnt_info:
        sales_info = list(zip(li, emoticons))
        pls_cnt = 0
        tot_price = 0
        for user in users:
            each_price = 0
            for info in sales_info:
                if info[0] >= user[0]:
                    each_price += (100 - info[0]) * info[1] // 100
            if each_price >= user[1]:
                pls_cnt += 1
                each_price = 0
            
            tot_price += each_price
        if pls_cnt > answer[0]:
            answer = [pls_cnt, tot_price]
            
        elif pls_cnt == answer[0]:
            if tot_price > answer[1]:
                answer = [pls_cnt, tot_price]
                
    return answer