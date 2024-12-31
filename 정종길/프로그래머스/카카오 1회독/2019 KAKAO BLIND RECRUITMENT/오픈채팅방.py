def solution(record):
    answer = []
    users = {}
    orders = []
    
    for rec in record:
        li = rec.split()
        
        if li[0][0] == "C":
            users[li[1]] = li[2]
            
        elif li[0][0] == "L":
            orders.append((li[0][0], li[1]))

        else:
            users[li[1]] = li[2]
            orders.append((li[0][0], li[1]))
    
    for cha, login_id in orders:
        if cha == "E":
            answer.append(f'{users[login_id]}님이 들어왔습니다.')
        else:
            answer.append(f'{users[login_id]}님이 나갔습니다.')
        
    return answer