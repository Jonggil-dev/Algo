
def solution(diffs, times, limit):
    answer = 1e9
    fault_times = [times[0]]
    
    for i in range(1, len(times)):
        fault_times.append(times[i-1] + times[i])
        
    start = 1
    end = 100000
    
    while start <= end:
        time = 0
        mid = (start + end) // 2
        
        for j in range(len(diffs)):
            if mid >= diffs[j]:
                time += times[j]
            else:
                time += (diffs[j] - mid) * fault_times[j] + times[j]
            
            if time > limit:
                break
        
        if time > limit:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid
        
    return answer
