'''
처음부터 짤라야 하는 조건 있는줄 모르고 다 풀었다가, 그냥 귀찮아서 필요한 부분만 수정함 -> 효율 별로니 2회차 풀이 볼 것것
'''

from collections import deque

def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, compress(s, i))
    return answer

def compress(s, ran):
    ans = ran
    repeat = deque(list(s[:ran]))
    pt, cnt = ran, 1
    
    while pt < len(s):
        if s[pt] == repeat[0]:
            if check(repeat, s, pt, ran):
                cnt += 1
                pt += ran
                continue
        
        if cnt > 1:
            ans += len(str(cnt))
            cnt = 1
        
        if pt + ran >= len(s):
            ans += len(s) - pt
            break
            
        for _ in range(ran):
            repeat.popleft()
            repeat.append(s[pt])
            ans += 1
            pt += 1
            
    if cnt > 1:
        ans += len(str(cnt))
    return ans

def check(reapeat, s, pt, ran):
    if pt + ran > len(s):
        return False
    
    for i in range(ran):
        if reapeat[i] != s[pt + i]:
            return False
    return True