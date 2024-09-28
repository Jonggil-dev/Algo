from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    bustime = 540  - t
    timetable = deque([int(human[:2]) * 60 + int(human[3:]) for human in sorted(timetable)])

    
    for i in range(n - 1):
        bustime += t
        for _ in range(m):
            if timetable:
                time = timetable.popleft()
                if time <= bustime:
                    continue
                else:
                    timetable.appendleft(time)
                    break
    
    bustime += t
    

    if len(timetable) >= m:
        if timetable[m - 1] <= bustime:
            bustime = timetable[m - 1] - 1

    answer = f'{bustime//60:02d}:{bustime%60:02d}'
        
    return answer

