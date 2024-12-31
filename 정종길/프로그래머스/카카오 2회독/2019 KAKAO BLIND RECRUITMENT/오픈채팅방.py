def solution(record):
    answer = []
    nick_infos = {}
    orders = []
    
    for rec in record:
        if rec[0] == "L":
            o, i = rec.split()
        else:
            o, i, n = rec.split()
            nick_infos[i] = n
        orders.append([o, i])
    
    for o, i in orders:
        if o[0] == "E":
            answer.append(f'{nick_infos[i]}님이 들어왔습니다.')
        elif o[0] == "L":
            answer.append(f'{nick_infos[i]}님이 나갔습니다.')
            
    return answer