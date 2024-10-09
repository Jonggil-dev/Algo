from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    info = defaultdict(int)
    t = date_to_int(today)
    
    for term in terms:
        alpha, month = term.split()
        info[alpha] = int(month)
    
    for i, privacy in enumerate(privacies):
        period, ty = privacy.split()
        p = date_to_int(period)
        p += (info[ty] * 28) - 1
        if p < t:
            answer.append(i + 1)
        
    return answer

def date_to_int(date):
    y, m, d = date.split(".")
    return int(y) * 12 * 28  + int(m) * 28 + int(d)