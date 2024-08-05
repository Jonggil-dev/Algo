def solution(play_time, adv_time, logs):
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    prefix = [0] * (play_time + 1)
    
    for log in logs:
        times = log.split("-")
        prefix[time_to_sec(times[0])] += 1
        prefix[time_to_sec(times[1])] -= 1
    
    for i in range(play_time):
        prefix[i + 1] += prefix[i]
        
    answer = 0
    st = 0
    et = adv_time
    max_v = running = sum(prefix[:adv_time])
    
    for j in range(adv_time, play_time + 1):
        running -= prefix[st]
        st += 1
        running += prefix[j]
        if max_v < running:
            max_v = running
            answer = st
    
    bh = answer // (60 * 60)
    bm = (answer % 3600) // 60
    bs = (answer % 3600) % 60
    
    return f"{bh:02}:{bm:02}:{bs:02}"

def time_to_sec(time):
    hh, mm, ss = map(int, time.split(":"))
    return hh * 3600 + mm * 60 + ss
    