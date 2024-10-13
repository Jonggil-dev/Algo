from collections import defaultdict

def solution(survey, choices):
    answer = ''
    scores = defaultdict(int)
    
    for i in range(len(survey)):
        c = choices[i]
        q, r = divmod(c, 4)
        if q == 0:
            scores[survey[i][0]] += (4 - r)
        else:
            scores[survey[i][1]] += r
    

    answer += "R" if scores["R"] >= scores["T"] else "T"
    answer += "C" if scores["C"] >= scores["F"] else "F"
    answer += "J" if scores["J"] >= scores["M"] else "M"
    answer += "A" if scores["A"] >= scores["N"] else "N"
    
    return answer