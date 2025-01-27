def solution(m, musicinfos):
    answer = ["(None)", -1]
    m = m.replace("C#", "H").replace("D#", "I").replace("F#", "J").replace("G#", "K").replace("A#", "L").replace("B#", "M")
    
    for info in musicinfos:
        st, et, t, mi = info.split(",")
        minutes = time_to_min(st, et)
        mi = mi.replace("C#", "H").replace("D#", "I").replace("F#", "J").replace("G#", "K").replace("A#", "L").replace("B#", "M")
        
        if answer[1] >= minutes:
            continue
            
        q, r = divmod(minutes, len(mi))
        melodys = mi * q + mi[:r]
        
        if m in melodys:
            answer = [t, minutes]
            
    return answer[0]

def time_to_min(st, et):
    sh, sm = st.split(":")
    eh, em = et.split(":")
        
    return int(eh) * 60 + int(em) - int(sh) * 60 - int(sm)
    