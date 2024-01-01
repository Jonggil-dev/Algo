def solution(m, musicinfos):
    answer='(None)'
    stime=0
    m=m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    for musicinfo in musicinfos:
        st,end,title,line=musicinfo.split(',')
        line=line.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
        st=st.split(':')
        end=end.split(':')
        time = (int(end[0]) - int(st[0])) * 60 + int(end[1]) - int(st[1])
        t = line*(time//len(line))+line[0:time % len(line)]
        if m in t and stime<time:
            answer=title
            stime=time

    return answer
