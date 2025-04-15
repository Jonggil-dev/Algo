'''
1. 전파가 닿지 않는 구간의 범위를 구하기
2. w * 2 + 1로 나누어 answer 구하기
'''

def solution(n, stations, w):
    answer = 0
    no_reaches = [] 
    no_reaches.append((stations[0] - w) - 1)
    for i in range(1, len(stations)):
        no_reaches.append((stations[i] - w) - (stations[i - 1] + w + 1))
    no_reaches.append(n - (stations[-1] + w))
    
    for ra in no_reaches:
        if ra <= 0:
            continue
        q, r = divmod(ra, w * 2 + 1)
        
        if r:
            answer += q + 1
        else:
            answer += q
            
    return answer
