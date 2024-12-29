from collections import Counter

def solution(N, stages):
    failures = []
    answer = []
    
    test = Counter(stages)
    persons = len(stages)
    cumulative_person = 0
    
    for i in range(1, N + 1):
        cumulative_person += test[i - 1]
        
        if(persons - cumulative_person <= 0):
            failures.append((0, i))
            continue
            
        failures.append((test[i] / (persons - cumulative_person) , i))

    failures.sort(key = lambda x : (-x[0], [1]))
    for _ , idx in failures:
        answer.append(idx)
        
    return answer