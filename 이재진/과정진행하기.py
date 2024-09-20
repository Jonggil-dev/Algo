def solution(plans):
    answer = []
    n = len(plans)
    
    dic = {}
    for i in range(len(plans)):
        hour, minute = plans[i][1].split(":")
        plans[i][1] = int(hour) * 60 + int(minute)
        plans[i][2] = int(plans[i][2])
        dic[plans[i][1]] = [plans[i][0], plans[i][2]]
    

    stack = []
    time = min(dic.keys())
    now = None
    need = 0
    while True:
        if len(answer) == n:
            break
        
        if now != None and need > 0:
            need -= 1
            if need == 0:
                answer.append(now)
                now = None
        
        if time in dic.keys():
            if now == None and need == 0:
                now, need = dic[time]
            else:
                stack.append([now, need])
                now, need = dic[time]
        else:
            if now == None and need == 0 and stack:
                now, need = stack.pop()
        time += 1
    return answer
