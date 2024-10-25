def solution(record):
    answer = []
    dic = {}
    cnt = 0
    for r in record:
        info = r.split(" ")
        status = info[0]
        uid = info[1]
        if len(info) == 3:
            name = info[2]
            dic[uid] = name
        
        
        if status == "Enter":
            answer.append([uid, " 들어왔습니다."])
        elif status == "Leave":
            answer.append([uid, " 나갔습니다."])
    
    for i in range(len(answer)):
        uid, string = answer[i][0], answer[i][1]
        tmp = dic[uid]+"님이"+string
        answer[i] = tmp
        
    return answer
