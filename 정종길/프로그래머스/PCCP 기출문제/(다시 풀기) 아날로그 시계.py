def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start_time = h1 * 60 * 60 + m1 * 60 + s1
    end_time = h2 * 60 * 60 + m2 * 60 + s2
    
    if start_time == 0 or start_time == 12 * 3600:
        answer += 1
        
    while start_time < end_time:

        h = start_time / 120 % 360
        m = start_time / 10 % 360
        s = start_time * 6 % 360
    
        n_h = 360 if (start_time + 1) / 120 % 360 == 0 else (start_time + 1) / 120 % 360
        n_m = 360 if (start_time + 1) / 10 % 360 == 0 else (start_time + 1) / 10 % 360
        n_s = 360 if (start_time + 1) * 6 % 360 == 0 else (start_time + 1) * 6 % 360
        
        if s < h and n_h <= n_s:
            answer += 1
        if s < m and n_m <= n_s:
            answer += 1

        if n_s == n_m and n_s == n_h:
            answer -= 1
            
        start_time += 1
    return answer