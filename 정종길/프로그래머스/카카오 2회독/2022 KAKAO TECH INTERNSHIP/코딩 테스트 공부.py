import heapq

def solution(alp, cop, problems):    
    alp_max = max(problems, key = lambda x : x[0])[0]
    cop_max = max(problems, key = lambda x : x[1])[1]
    
    time_table = [[1e9] * (cop_max + 1) for _ in range(alp_max + 1)]
    
    q = [(0, min(alp, alp_max), min(cop, cop_max))]
    
    while q:
        t, ha, hc = heapq.heappop(q)
        
        if t > time_table[ha][hc]:
            continue
        
        for aq, cq, ar, cr, c in problems:
            if aq <= ha and cq <= hc:
                nar, ncr, nt = min(ha + ar, alp_max), min(hc + cr, cop_max), t + c
                if nt < time_table[nar][ncr]:
                    time_table[nar][ncr] = nt
                    heapq.heappush(q, (nt, nar, ncr))
        
        nar, ncr, nt = min(ha + 1, alp_max), min(hc, cop_max), t + 1
        if nt < time_table[nar][ncr]:
            time_table[nar][ncr] = nt
            heapq.heappush(q, (nt, nar, ncr))
            
        nar, ncr, nt = min(ha, alp_max), min(hc + 1, cop_max), t + 1
        if nt < time_table[nar][ncr]:
            time_table[nar][ncr] = nt
            heapq.heappush(q, (nt, nar, ncr))       
    
    return time_table[alp_max][cop_max]