def solution(diffs, times, limit):
    answer = 0
    n = len(diffs)
    start = 1
    end = max(diffs)
    while start < end:
        level = (start+end) // 2
        time = 0
        flag = False
        for i in range(n):
            if diffs[i] <= level:
                time += times[i]
            else:
                time += sum(times[i-1:i+1]) * (diffs[i]-level)
                time += times[i]
            if time > limit:
                flag = True
                break
        if not flag and time <= limit:
            end = level
        else:
            start = level + 1
    answer = (start+end) // 2
    return answer
