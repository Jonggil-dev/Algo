def solution(m, musicinfos):
    answer = []
    m = m.replace("A#", "H").replace("B#", "I").replace("C#", "J").replace("D#", "K").replace("F#", "L").replace("G#", "M")
    
    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(",")
        diff = diff_minutes(start_time, end_time)
        melody = melody.replace("A#", "H").replace("B#", "I").replace("C#", "J").replace("D#", "K").replace("F#", "L").replace("G#", "M")
        tmp = ""
        
        for j in range(diff):
            tmp += melody[j % len(melody)]
        
        if m in tmp:
            answer.append((diff, title))
                
    if not answer:
        return "(None)"
    else:
        answer.sort(key = lambda x : -x[0])
        return answer[0][1]

def diff_minutes(start, end):
    end_h, end_m = end.split(":")
    start_h, start_m = start.split(":")
    
    return 60 * (int(end_h) - int(start_h)) + (int(end_m) - int(start_m))