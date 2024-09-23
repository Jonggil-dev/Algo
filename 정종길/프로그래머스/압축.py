def solution(msg):
    answer = []
    dic = {}
    
    for i in range(26):
        dic[chr(65 + i)] = i + 1
    
    cnt = 27
    i = 0
    search = ''
    
    while i < len(msg):
        search += msg[i]
        
        if search in dic:
            i += 1
            continue
            
        else:
            dic[search] = cnt
            cnt += 1
            s = search[:-1]
            answer.append(dic[s])
            search = ''
            
    answer.append(dic[search])
    return answer