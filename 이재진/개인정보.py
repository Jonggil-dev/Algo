def solution(today, terms, privacies):
    today = list(map(int, today.split('.')))
    answer = []
    dic = {}
    for i in terms:
        a, b = i.split()
        dic[a] = int(b)
    
    for num, i in enumerate(privacies):
        date, t = i.split()
        year, month, day = map(int, date.split('.'))
        year += dic[t]//12
        month += dic[t]%12
        day -= 1
        
        
        
        if month > 12:
            year += month//12
            month = month%12
        if day == 0:
            day = 28
            month -= 1
        if month == 0:
            month = 12
            year -= 1
        
        print(year, month, day)
        for k, l in zip([year, month, day], today):
            if k < l:
                answer.append(num+1)
                break
            elif k > l:
                break
            
    return answer
