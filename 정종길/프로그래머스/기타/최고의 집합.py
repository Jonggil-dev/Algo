def solution(n, s):
    q, r = divmod(s, n)
    
    if q == 0:
        return [-1]
    
    answer = [q] * n
    
    for i in range(1, r + 1):
        answer[-i] += 1
        
    return answer