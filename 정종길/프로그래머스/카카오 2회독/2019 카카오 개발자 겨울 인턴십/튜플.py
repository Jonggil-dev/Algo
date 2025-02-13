def solution(s):
    answer = []
    s_li = s.replace("{", " ").replace("}", " ").strip().split(" , ")
    
    record = set()
    s_li.sort(key = lambda x : len(x))
    
    for data in s_li:
        tmp = map(int, data.split(","))
        for num in tmp:
            if num not in record:
                answer.append(num)
                record.add(num)
    
    return answer