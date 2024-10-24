def solution(play_time, adv_time, logs):
    ps, ads = toSec(play_time), toSec(adv_time) - 1
    prefix_sums = [0] * (ps + 1)

    for log in logs:
        s, e = log.split("-")
        prefix_sums[toSec(s)] += 1
        prefix_sums[toSec(e)] -= 1
    
    for i in range(ps):
        prefix_sums[i + 1] += prefix_sums[i]
    
    answer = 0
    i, j = 0, ads
    max_v = tot = sum(prefix_sums[i : j + 1])
    
    while j < ps:
        j += 1
        tot  += prefix_sums[j] - prefix_sums[i]
        i += 1
        if tot > max_v:
            max_v = tot
            answer = i
            
    hh, mm, ss = tohhmmss(answer)
    return f'{hh:02d}:{mm:02d}:{ss:02d}'

def toSec(txt):
    hh, mm, ss = txt.split(":")
    return int(hh) * 3600 + int(mm) * 60 + int(ss)

def tohhmmss(second):
    hh = second // 3600
    mm = (second % 3600) // 60
    ss = second % 60
    return hh, mm, ss