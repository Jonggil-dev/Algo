def solution(lines):
    answer = 1
    times = []
    for line in lines:
        _, datetime, play = line.split()
        times.append(to_sec(datetime, play))

    i = 0
    while i < len(times):
        cnt = 1
        head = times[i][1]
        tail = head + 1000
        j = i + 1
        while j < len(times):
            ns, ne = times[j][0], times[j][1]
            if ns < tail and head <= ne:
                cnt += 1
            j += 1
        i += 1
        answer = max(answer, cnt)
        
    return answer

def to_sec(datetime, play):
    h, m, s = datetime.split(":")
    end = int(h) * 3600000 + int(m) * 60000 + float(s) * 1000
    start = end - (float(play[:-1]) * 1000) + 1
    return (start, end)
