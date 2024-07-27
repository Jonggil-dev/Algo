import heapq

def solution(alp, cop, problems):
    max_alp = max(problems)[0]
    max_cop = max(problems, key = lambda x:x[1])[1]
    
    max_alp = max(alp, max_alp)
    max_cop = max(cop, max_cop)
    
    arr_dp = [[1e9] * (max_cop + 1) for _ in range(max_alp + 1)]
    
    q = [(0, alp, cop)]
    arr_dp[alp][cop] = 0
    
    while q:
        time, alp, cop = heapq.heappop(q)
    
        if time > arr_dp[alp][cop]:
            continue
        
        if alp + 1 <= max_alp:
            if time + 1 < arr_dp[alp + 1][cop]:
                arr_dp[alp + 1][cop] = time + 1
                heapq.heappush(q, (time + 1,  min(alp + 1, max_alp), cop))
        
        if cop + 1 <= max_cop:
            if time + 1 < arr_dp[alp][cop + 1]:
                arr_dp[alp][cop + 1] = time + 1
                heapq.heappush(q, (time + 1,  alp, min(cop + 1, max_cop)))
                           
        for problem in problems:
            if alp >= problem[0] and cop >= problem[1]:
                new_alp, new_cop, new_time = min(alp + problem[2], max_alp), min(cop + problem[3], max_cop), time + problem[4]
                if new_time < arr_dp[new_alp][new_cop]:
                    arr_dp[new_alp][new_cop] = new_time
                    heapq.heappush(q, (new_time, new_alp, new_cop))
                    
    return arr_dp[max_alp][max_cop]