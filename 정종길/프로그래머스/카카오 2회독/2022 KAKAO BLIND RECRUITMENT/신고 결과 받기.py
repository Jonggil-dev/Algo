from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    alerted = defaultdict(int)
    
    for re in set(report):
        h = re.split()[1]
        alerted[h] += 1
    
    for re in set(report):
        h1, h2 = re.split()
        if alerted[h2] >= k:
            i = id_list.index(h1)
            answer[i] += 1
            
    return answer