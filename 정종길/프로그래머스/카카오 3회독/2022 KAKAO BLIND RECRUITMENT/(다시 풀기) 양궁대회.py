'''
완전 탐색
-> 라이언이 획득 할 수 있는 점수
-> 각 점수(0 ~ 10)를 획득하냐 못하냐로 따졌을 때 2 ^ 11 가지
-> 2 ^ 11 가지에 대해 어피치의 과녁을 토대로 점수에 해당하는 라이언의 과녁 완성
-> 완성된 과녁의 화살의 갯수 + 어피치와의 점수 차이 계산 해서 유효성 평가

최악의 연산 : (2 ^ 11)  * 11(라이억 과녁 완성을 위한 순회 및 어피치와의 점수 차이 계산) -> 2~3만 -> 충분
'''

def solution(n, info):
    global answer, max_diff
    
    answer, combs, appeach_score, max_diff = [], [], 0, -1
    make_combs("", 0, combs)
    combs.sort(reverse=True)
    
    for i in range(11):
        if info[i]:
            appeach_score += 10 - i
    
    for comb in combs:
        make_ryan(n, comb, info, appeach_score)
    
    if not answer:
        return [-1]
    
    answer.sort(key = lambda x : (-x[10], -x[9], -x[8], -x[7], -x[6],-x[5], -x[4],-x[3], -x[2],-x[1], -x[0]))
    
    return answer[0]

def make_combs(comb, cnt, combs):
    if cnt == 11:
        combs.append(comb)
        return
    
    make_combs(comb + "0", cnt + 1, combs)
    make_combs(comb + "1", cnt + 1, combs)
    return


def make_ryan(n, comb, appeach_info, appeach_score):
    global answer, max_diff
    
    ryan_info = []
    ryan_score = 0
    
    for idx in range(11):
        if comb[idx] == "1":
            arrows = appeach_info[idx] + 1
            n -= arrows
            ryan_info.append(arrows)
            ryan_score += (10 - idx)
            
            if appeach_info[idx]:
                appeach_score -= (10 - idx)
                
        else:
            ryan_info.append(0)
        
        if n < 0:
            return False
        
    if appeach_score >= ryan_score or (ryan_score - appeach_score) < max_diff:
        return False
    
    
    if n > 0:
        ryan_info[-1] += n
    
    if (ryan_score - appeach_score) > max_diff:
        answer = []
        
    max_diff = max(max_diff, ryan_score - appeach_score)
    answer.append(ryan_info)
    